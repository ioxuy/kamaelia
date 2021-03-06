#!/usr/bin/env python2.3
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

The usual method of sending a producerFinished/shutdown to the "control"
inbox is used to shut it down

This component does not terminate.
"""

from Axon.Component import component
from Axon.Ipc import producerFinished, shutdown

import string

class CharacterFIFO(object):
    def __init__(self):
        self.queuearray = []
        self.length = 0
        self.startboundary = 0
        
    def push(self, text):
        self.queuearray.append(text)
        self.length += len(text)
        
    def __len__(self):
        return self.length
        
    def poplength(self, length):
        if len(self) < length:
            raise IndexError
        else:
            thischunk = []
            sizeneeded = length
            while 1:
                chunk = self.queuearray[0]
                sizeneeded -= len(chunk) - self.startboundary
                
                if sizeneeded < 0: # new start boundary in the middle of this chunk
                    thischunk.append(chunk[self.startboundary:len(chunk) + sizeneeded])
                    self.startboundary = len(chunk) + sizeneeded
                else: # this chunk is completely within the requested string
                    if self.startboundary > 0:
                        thischunk.append(chunk[self.startboundary:])
                    else:
                        thischunk.append(chunk)
                    
                    self.queuearray.pop(0)
                    self.startboundary = 0
                    
                if sizeneeded <= 0:
                    break

            self.length -= length
            return string.join(thischunk, "")
    
class Chunkifier(component):
    """\
    Chunkifier([chunksize]) -> new Chunkifier component.
    
    Flow controller - collects incoming data and outputs it only as quanta of
    a given length in bytes (chunksize), unless the input stream ends (producerFinished). 
    
    Keyword arguments:
    - chunksize  -- Chunk size in bytes
    """
    
    Inboxes = { "inbox" : "Data stream to be split into chunks",
                "control": "UNUSED" }
    Outboxes = { "outbox" : "Each message is a chunk",
                "signal": "UNUSED" }

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
                self.forwardqueue.push(msg)
            
            while len(self.forwardqueue) >= self.chunksize:
                self.sendChunk()
                
            if self.nodelay:
                self.sendPartialChunk()
                
            while self.dataReady("control"):
                msg = self.recv("control")
                if isinstance(msg, producerFinished):
                    self.sendPartialChunk()
                    self.send(msg, "signal")
                    return
                elif isinstance(msg, shutdown):
                    self.send(msg, "signal")
                    return
            self.pause()

if __name__ == '__main__':
    from Kamaelia.Util.PipelineComponent import pipeline
    from Kamaelia.Util.Console import ConsoleEchoer, ConsoleReader

    pipeline(
        ConsoleReader(eol=""),
        Chunkifier(20),
        ConsoleEchoer()
    ).run()
