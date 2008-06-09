import Axon
from Axon.Ipc import shutdown

from TorrentService import TorrentService
from TorrentIPC import *

"""\
=================
TorrentPatron - a BitTorrent Client
=================

State of development: BETA
Known quirks: Clear out your ~/.bittorrent/ directory if you get errors
about torrents including files that are part of other torrents.

This component is for downloading and uploading data using the peer-to-peer
BitTorrent protocol.

Use this component in preference to TorrentClient.

This component uses a TorrentService component to co-ordinate the sharing
of a single TorrentClient between many TorrentPatrons. This is necessary
as running more than one instance of TorrentClient will fail
(see TorrentClient.py for a full explanation).

How does it work?
-----------------

When TorrentPatron is first run, it will get a TorrentService object -
if one already exists it will pick that, otherwise it will create a new one.
It then registers itself with this service allowing it to receive messages
from it. Messages TorrentPatron receives on its inbox are forwarded to 
TorrentService (in a TIPCServicePassOn wrapper) which in turn forwards them to
TorrentClient. Messages generated by TorrentClient relevant to the torrents
started by this instance of TorrentPatron are forwarded to it by TorrentService.

The result of this is that inboxes/outboxes used and the IPC messages accepted/
produced are identical to TorrentClient.

These IPC messages may be found in TorrentIPC.py

Those used internally:
* TIPCServicePassOn - used to wrap messages from TorrentPatron for TorrentClient
* TIPCServiceAdd - register this TorrentPatron with a TorrentService
* TIPCServiceRemove - deregister this TorrentPatron with a TorrentService

Those used externally (i.e. seen/sent by user components):

- Send to TorrentPatron:
  * TIPCCreateNewTorrent - start a new torrent from the contents of a .torrent file
  * TIPCCloseTorrent - stop a running torrent
  
- Sent by TorrentPatron:
  * TIPCNewTorrentCreated - a new torrent has been started from your (oldest) TIPCCreateNewTorrent message
  * TIPCTorrentStartFail - the torrent associated with your (oldest) TIPCCreateNewTorrent message could not be started
  * TIPCTorrentAlreadyDownloading - the torrent associated with your (oldest) TIPCCreateNewTorrent message is already downloading
  * TIPCTorrentStatusUpdate - a status object for one of your active torrents
"""

class TorrentPatron(Axon.Component.component):
    Inboxes = {
        "inbox"          : "Commands for the TorrentClient",
        "torrent-inbox"  : "Received feedback from TorrentClient",
        "control"        : "Shut me down"
    }
                 
    Outboxes = {
        "outbox"         : "Forward feedback from TorrentClient out of",
        "torrent-outbox" : "Talk to TorrentClient with",
        "signal"         : "UNUSED"
    }
                 
                
    def main(self):
        """Main loop of TorrentPatron"""
        
        torrentService, torrentShutdownService, newTorrentService = TorrentService.getTorrentServices(self.tracker)
        if newTorrentService:
            newTorrentService.activate()
            self.addChildren(newTorrentService)

        self.link((self, "torrent-outbox"), torrentService)
        self.send(TIPCServiceAdd(replyService=(self, "torrent-inbox")), "torrent-outbox")
        
        loop = True
        while loop:
            #print "TorrentPatron.main loop"
            yield 1
            
            if self.dataReady("inbox"):
                #print "TorrentPatron inbox"            
                msg = self.recv("inbox")
                msg = TIPCServicePassOn(replyService=(self, "torrent-inbox"), message=msg)
                self.send(msg, "torrent-outbox")
                
            elif self.dataReady("torrent-inbox"):
                msg = self.recv("torrent-inbox")
                #print "TorrentPatron torrent-inbox"
                #print msg
                self.send(msg, "outbox")
                
            elif self.dataReady("control"):
                #print "TorrentPatron control"            
                msg = self.recv("control")
                if isinstance(msg, shutdown):
                    loop = False
                    
            else:
                self.pause()
            
            
        #unregister with the service
        self.send(TIPCServiceRemove(replyService=(self, "torrent-inbox")), "torrent-outbox")
        
__kamaelia_components__  = ( TorrentPatron, )