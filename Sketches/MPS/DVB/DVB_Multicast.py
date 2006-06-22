#!/usr/bin/python
#
# This code is designed soley for the purposes of demonstrating the tools
# for timeshifting.
#

import dvb3
from Axon.Component import component
from Kamaelia.Device.DVB.Core import DVB_Multiplex
from Kamaelia.Util.PipelineComponent import pipeline
from Kamaelia.Internet.Multicast_transceiver import Multicast_transceiver
from Kamaelia.File.Writing import SimpleFileWriter
from Kamaelia.ReadFileAdaptor import ReadFileAdaptor

# from Kamaelia.File.Writing import SimpleFileWriter
# from Kamaelia.File.UnixPipe import Pipethrough

freq = 754.166670
feparams = {
    "inversion" : dvb3.frontend.INVERSION_AUTO,
    "constellation" : dvb3.frontend.QAM_16,
    "coderate_HP" : dvb3.frontend.FEC_3_4,
    "coderate_LP" : dvb3.frontend.FEC_3_4,
}
service_ids = { "BBC ONE": 4168,
                "BBC TWO": 4232,
                "CBEEBIES":16960,
                "CBBC":4671,
              }

class detuple(component):
   def __init__(self, index):
      super(detuple, self).__init__()
      self.index = index
   def main(self):
      while 1:
         if self.dataReady("inbox"):
            tuple=self.recv("inbox")
            self.send(tuple[self.index], "outbox")
         yield 1

class blockise(component):
    def main(self):
       maxlen = 1000 # Needs to be parameterisable
       buffer = ""
       while 1:
           while self.dataReady("inbox"):
               buffer = buffer + self.recv("inbox")
               if len(buffer) > maxlen:
                  send = buffer[:maxlen]
                  buffer = buffer[maxlen:]
               else:
                  send = buffer
                  buffer = ""
               self.send(send, "outbox")
           yield 1

class counter(component):
    def __init__(self, tag):
        super(counter, self).__init__()
        self.tag = tag
    def main(self):
        count = 0
        while 1:
            while self.dataReady("inbox"):
                self.send(self.recv("inbox"), "outbox")
                count = count +1
            print self.tag, ":", count
            self.pause()
            yield 1

if 1:
    pipeline(
        DVB_Multiplex(freq, [600,601], feparams),
        SimpleFileWriter("somefile.ts"),
    ).run()

if 0:
    pipeline(
        ReadFileAdaptor("somefile.ts",readsize=8000000),
        blockise(),
        Multicast_transceiver("0.0.0.0", 0, "224.168.2.9", 1600),
    ).activate()

    pipeline(
        Multicast_transceiver("0.0.0.0", 1600, "224.168.2.9", 0),
        detuple(1),
        SimpleFileWriter("otherfile.ts"),
    ).run()
