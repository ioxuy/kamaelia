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

from Axon.Component import component
from Axon.Ipc import shutdownMicroprocess, producerFinished

import pymedia.muxer as muxer
import pymedia.audio.acodec as acodec

import sys,os
sys.path.append(__file__[:1+__file__.rfind(os.sep)] + (".."+os.sep)*3)
from Support.PyMedia.AudioFormats import format2PyMediaFormat
from Support.PyMedia.AudioFormats import codec2PyMediaCodec


class Encoder(component):
    def __init__(self, codec, bitrate, sample_rate, channels, **otherparams):
        """x.__init__(...) initializes x; see x.__class__.__doc__ for signature"""
        super(Encoder,self).__init__()

        codec = codec2PyMediaCodec[codec]
        
        params = { 'id'          : acodec.getCodecID(codec),
                   'bitrate'     : bitrate,
                   'sample_rate' : sample_rate,
                   'channels'    : channels 
                 }
        params.update(otherparams)
                 
        self.params = params
        self.codec = codec
        
    def main(self):
        mux = muxer.Muxer( self.codec )
        streamId = mux.addStream( muxer.CODEC_TYPE_AUDIO, self.params )
        enc = acodec.Encoder(self.params)
        
        data = mux.start()
        if data:
            self.send(data,"outbox")
        
        shutdown=False
        data=""
        MINSIZE=4096
        while self.anyReady() or not shutdown:
            while self.dataReady("inbox"):
                newdata= self.recv("inbox")
                data = data+newdata
                if len(data)>=MINSIZE:
                    frames = enc.encode( data )
                    
                    for frame in frames:
                        muxed = mux.write( streamId, frame )
                        if muxed:
                            self.send(muxed, "outbox")
                            
                    data=""
        
            while self.dataReady("control"):
                msg=self.recv("control")
                if isinstance(msg, (producerFinished,shutdownMicroprocess)):
                    shutdown=True
                self.send(msg,"signal")
                
            if not shutdown:
                self.pause()
            yield 1
        
        data = mux.end()
        if data:
            self.send(data,"outbox")
