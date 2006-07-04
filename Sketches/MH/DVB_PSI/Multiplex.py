#!/usr/bin/env python

# an attempt at a new 'multiplex' component (arguable a tuner)
# that uses subscriptions to manage the demuxing filters


import os
import dvb3.frontend
import dvb3.dmx
import time
import struct

from Axon.Component import component
from Axon.ThreadedComponent import threadedcomponent
from Axon.Ipc import shutdownMicroprocess,producerFinished
from Axon.AxonExceptions import ServiceAlreadyExists
from Axon.CoordinatingAssistantTracker import coordinatingassistanttracker as CAT


DVB_PACKET_SIZE = 188
DVB_RESYNC = "\x47"
import Axon.AdaptiveCommsComponent
    
class DVB_Multiplex(threadedcomponent):
    """\
    This is a DVB Multiplex Tuner.

    This tunes the given DVB card to the given frequency. This then sets
    up the dvr0 device node to recieve the data recieved on a number of
    PIDs.

    A special case use of these is to tune to 2 specific PIDs - the audio
    and video for a specific TV channel. If you pass just 2 PIDs then
    you're tuning to a specific channel.

    NOTE 1: This multiplex tuner deliberately does not know what
    frequency the multiplex is on, and does not know what PIDs are
    inside that multiplex. You are expected to find out this information
    independently.

    NOTE 2: This means also that producing a mock for the next stages in
    this system should be relatively simple - we run this code once and
    dump to disk. 
    """
    def __init__(self, freq, feparams={}, called=None):
        self.freq = freq
        self.feparams = feparams
        super(DVB_Multiplex, self).__init__()
        
        if called:
            self.servicename = called
            cat = CAT.getcat()
            try:
                cat.registerService(self.servicename, self, "inbox")
            except Axon.AxonExceptions.ServiceAlreadyExists, e:
                print "***************************** ERROR *****************************"
                print "An attempt to make a 2nd DVB_Multiplex with the same name happened."
                print "This is incorrect usage."
                print 
                traceback.print_exc(3)
                print "***************************** ERROR *****************************"
    
                raise e
    
    
    def shutdown(self):
        while self.dataReady("control"):
            msg = self.recv("control")
            self.send(msg,"signal")
            if isinstance(msg, (shutdownMicroprocess, producerFinished)):
                return True
        return False

    def main(self):
        # Open the frontend of card 0 (/dev/dvb/adaptor0/frontend0)
        self.fe = dvb3.frontend.Frontend(0, blocking=0)
        self.tune_DVBT(self.freq, self.feparams)
        
        while self.notLocked():
            time.sleep(0.1)
            #yield 1  # could sleep for, say, 0.1 seconds.
            
        demuxers = {}
        
        # This is then a file reader, actually.
        # Should be a little more system friendly really
        fd = os.open("/dev/dvb/adapter0/dvr0", os.O_RDONLY) # | os.O_NONBLOCK)
        while not self.shutdown():
            
            while self.dataReady("inbox"):
                cmd = self.recv("inbox")
                demuxers = self.handleCommand(cmd, demuxers)
            
            if demuxers:
                try:
                    data = os.read(fd, 2048)
                    self.send(data, "outbox")
                except OSError:
                    pass
            else:
                self.sync()


    def tune_DVBT(self, frequency, feparams={}):
        # Build the tuning parameters (DVB-T)
        params = dvb3.frontend.OFDMParameters()
        params.frequency = frequency * 1000 * 1000
        # load up any extra params specified for the frontend
        for key in feparams:
            params.__dict__[key] = feparams[key]
    
        # Start the tuning
        self.fe.set_frontend(params)
        
    
    def notLocked(self):
        """\
        Wait for lock, if it's not available, yield a true value.
        If it is, exit with a StopIteration. (allows use in a for
        loop)
        """
        return (self.fe.read_status() & dvb3.frontend.FE_HAS_LOCK) != 0
    
    def addPID(self,pid):
        """\
        Adds the given PID to the transport stream that will be available
        in "/dev/dvb/adapter0/dvr0"
        """
        demuxer = dvb3.dmx.Demux(0, blocking = 0)
        demuxer.set_pes_filter( pid,
                                dvb3.dmx.DMX_IN_FRONTEND,
                                dvb3.dmx.DMX_OUT_TS_TAP,
                                dvb3.dmx.DMX_PES_OTHER,
                                dvb3.dmx.DMX_IMMEDIATE_START )
        return demuxer
    
    
    def handleCommand(self,cmd,demuxers):
        if cmd[0] == "ADD":
            pidlist = cmd[1]          # dest = (component,inboxname)
            
            for pid in pidlist:
                if pid not in demuxers:
                    demuxers[pid] = self.addPID(pid)
                    
            return demuxers
            
        elif cmd[0] == "REMOVE":
            pidlist = cmd[1]
            
            for pid in pidlist:
                if pid in demuxers:
                    demuxers[pid].stop()
                    del demuxers[pid]
                    
            return demuxers

if __name__=="__main__":
    
    import random

    class Subscriber(component):
        def __init__(self, servicename, spacing, *pids):
            super(Subscriber,self).__init__()
            self.notsubscribed = list(pids)
            self.subscribed = []
            self.spacing = " "*spacing
            self.servicename = servicename
            
        def takesomefrom(self,source):
            items = []
            if len(source):
                qty = 1+random.randrange(0,len(source))
                for _ in range(0,qty):
                    i = random.randrange(0,len(source))
                    items.append(source[i])
                    del source[i]
            return items
                
        def changeSubscription(self):
            if random.randrange(0,2) == 1:
                pids = self.takesomefrom(self.notsubscribed)
                self.send( ("ADD",(self,"inbox"),pids), "outbox")
                self.subscribed.extend(pids)
            else:
                pids = self.takesomefrom(self.subscribed)
                self.send( ("REMOVE",(self,"inbox"),pids), "outbox")
                self.notsubscribed.extend(pids)
            print self.spacing,"Now subscribed to pids:"
            print self.spacing,"  ",self.subscribed
                
        def main(self):
            cat = CAT.getcat()
            service = cat.retrieveService(self.servicename)
            self.link((self,"outbox"),service)
            
            nextchangetime = self.scheduler.time + random.randrange(5,10)
            self.notyetreceived = self.subscribed[:]
            while 1:
                while self.dataReady("inbox"):
                    packet = self.recv("inbox")
                    pid = ((ord(packet[1]) << 8) + ord(packet[2])) & 0x1fff
                    if pid not in self.subscribed:
                        print self.spacing,"Shouldn't have received pid:",pid
                    else:
                        if pid in self.notyetreceived:
                            print self.spacing,"Received 1st of pid:",pid
                            self.notyetreceived.remove(pid)
                        
                if self.scheduler.time >= nextchangetime:
                    nextchangetime = self.scheduler.time + random.randrange(10,20)
                    self.changeSubscription()
                    self.notyetreceived = self.subscribed[:]
                
                if self.subscribed:
                    self.pause()
                yield 1
                
                
                
    class DVB_PacketAligner(component):
        def shutdown(self):
            while self.dataReady("control"):
                msg = self.recv("control")
                self.send(msg,"signal")
                if isinstance(msg, (shutdownMicroprocess, producerFinished)):
                    self.shuttingdown=True
            return self.shuttingdown
        
        def main(self):
            buffer = ""
            buffers = []
            self.shuttingdown=False
            
            while not self.shutdown():
                
                while self.dataReady("inbox"):
                    buffers.append(self.recv("inbox"))
                    
                while len(buffers)>0:
                    
                    if len(buffer) == 0:
                        buffer = buffers.pop(0)
                    else:
                        buffer += buffers.pop(0)
        
                    while len(buffer) >= DVB_PACKET_SIZE:
                        i = buffer.find(DVB_RESYNC)
                        if i == -1: # if not found
                            "we have a dud"
                            buffer = ""
                            continue
                        if i>0:
                            # if found remove all bytes preceeding that point in the buffers
                            # And try again
                            buffer = buffer[i:]
                            continue
                        # packet is the first 188 bytes in the buffer now
                        packet, buffer = buffer[:DVB_PACKET_SIZE], buffer[DVB_PACKET_SIZE:]
        
                        self.send(packet, "outbox")
                            
                self.pause()
                yield 1

    from Kamaelia.Chassis.Pipeline import pipeline
    from Kamaelia.Chassis.Graphline import Graphline
    from Demuxer import DVB_Demuxer
    
    feparams = {
        "inversion" : dvb3.frontend.INVERSION_AUTO,
        "constellation" : dvb3.frontend.QAM_16,
        "coderate_HP" : dvb3.frontend.FEC_3_4,
        "coderate_LP" : dvb3.frontend.FEC_3_4,
    }

    print "---1st subscriber:------|---2nd subscriber:------"
    
    Subscriber("MUX1", 0,  0,0x11,0x12,600,601).activate()
    Subscriber("MUX1", 25, 0,0x11,0x12,600,601).activate()

    Graphline( MUX = DVB_Multiplex(505833330.0/1000000.0, feparams),
               DEMUX = DVB_Demuxer(called="MUX1"),
               linkages = {
                       ("DEMUX","pid_request") : ("MUX",  "inbox"),
                       ("MUX",  "outbox")      : ("DEMUX","inbox"),
                   }
             ).run()

#    pipeline( DVB_Multiplex(505833330.0/1000000.0, feparams, called="MUX1"),
#              DVB_PacketAligner(),
#              Subscriber("MUX1", 0,     0, 0x11, 0x12, 600, 601),
#            ).run()
