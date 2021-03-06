#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Copyright 2010 British Broadcasting Corporation and Kamaelia Contributors(1)
#
# (1) Kamaelia Contributors are listed in the AUTHORS file and at
#     http://www.kamaelia.org/AUTHORS - please extend this file,
#     not this notice.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
# -------------------------------------------------------------------------
# Licensed to the BBC under a Contributor Agreement: RJL

"""\
=========================
Chunkifier
=========================

A component that fixes the message size of an input stream to a given value,
outputting blocks of that size when sufficient input has accumulated. This
component's input is stream orientated - all messages received are
concatenated to the interal buffer without divisions.

Example Usage
-------------

Chunkifying a console reader::

pipeline(
    ConsoleReader(eol=""),
    Chunkifier(20),
    ConsoleEchoer()
).run()

How does it work?
-----------------

Messages received on the "inbox" are buffered until at least N bytes have
been collected. A message containing those first N bytes is sent out
"outbox". A CharacterFIFO object is used to do this in linear time.

The usual sending of a producerFinished/shutdown to the "control"
inbox will shut it down.
"""

from Axon.Component import component
from Axon.Ipc import producerFinished, shutdown

import string
from Kamaelia.Community.RJL.Kamaelia.Util.CharacterQueue import CharacterFIFO

class Chunkifier(component):
    """\
    Chunkifier([chunksize]) -> new Chunkifier component.
    
    Flow controller - collects incoming data and outputs it only as quanta of
    a given length in bytes (chunksize), unless the input stream ends (producerFinished). 
    
    Keyword arguments:
    - chunksize  -- Chunk size in bytes
    - nodelay    -- if set to True, partial chunks will be output rather
                    than buffering up data while waiting for more to arrive.
    """
    
    Inboxes = {
        "inbox" : "Data stream to be split into chunks",
        "control": "Shut me down"
    }
    Outboxes = {
        "outbox" : "Each message is a chunk",
        "signal": "I've shut down"
    }

    def __init__(self, chunksize = 1048576, nodelay = False):
        super(Chunkifier, self).__init__()
        self.forwardqueue = CharacterFIFO()
        self.chunksize = chunksize
        self.nodelay = nodelay
    
    def sendPartialChunk(self):
        if len(self.forwardqueue) > 0:
            self.send(self.forwardqueue.poplength(len(self.forwardqueue)), "outbox")
    
    def sendChunk(self):
        self.send(self.forwardqueue.poplength(self.chunksize), "outbox")

    def main(self):
        while 1:
            yield 1
            while self.dataReady("inbox"):
                msg = self.recv("inbox")
                
                # add this string to our character queue
                self.forwardqueue.push(msg)
            
            # while there is enough data to send another chunk
            while len(self.forwardqueue) >= self.chunksize:
                self.sendChunk()
            
            # if nodelay then send any data not yet sent rather than waiting for more
            if self.nodelay:
                self.sendPartialChunk()
                
            while self.dataReady("control"):
                msg = self.recv("control")
                if isinstance(msg, producerFinished):
                    self.sendPartialChunk()
                    self.send(producerFinished(self), "signal")
                    return
                elif isinstance(msg, shutdown):
                    self.send(producerFinished(self), "signal")
                    return
            self.pause()

__kamaelia_components__  = ( Chunkifier, )

if __name__ == '__main__':
    from Kamaelia.Chassis.Pipeline import pipeline
    from Kamaelia.Util.Console import ConsoleEchoer, ConsoleReader

    # Example - spit out text entered by the user in chunks of 10 characters
    pipeline(
        ConsoleReader(eol=""),
        Chunkifier(10),
        ConsoleEchoer()
    ).run()
