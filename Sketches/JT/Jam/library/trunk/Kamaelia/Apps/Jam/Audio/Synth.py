# -*- coding: utf-8 -*-
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

"""
=============
Synth Builder
=============

A simple component for connecting a polyphony component to a number of voices.  This means less typing is needed, and provides a simple way to encapsulate a synth system in a single component.  The component takes a generator as an argument which provides the Synth with its voices, allowing more flexibility in how which voices are used, and how they are created.

Example Usage
-------------
An 8 voice sine synth

def voiceGenerator():
    for i in range(8):
        yield SineVoice()

Pipeline(PianoRoll(),
         Synth(voiceGenerator, polyphony=8)).run()

How it works
------------
The component creates the polyphoniser, and links up its "inbox" inbox to the polyphoniser's "inbox" inbox.  It then loops over the voice generator, linking the voice outputs from the polyphoniser to the voices which are created.

"""
import Axon
from Kamaelia.Apps.Jam.Audio.Polyphony import Polyphoniser

class Synth(Axon.Component.component):
    """
    Synth(voiceGenerator, [polyphoniser, polyphony]) -> new Synth component
    
    Creates a synth system from a polyphony component and a number of generated
    voices

    Arguments:
    - voiceGenerator -- A generator which yields non-activated voice components

    Keyword Arguments:
    - polyphoniser -- The component to use as a polyphoniser
    - polyphony    -- The number of simultaneous voices the synth will have
    """

    polyphony = 8
    polyphoniser = Polyphoniser

    def __init__(self, voiceGenerator, **argd):
        """
        x.__init__(...) initializes x; see x.__class__.__doc__ for signature
        """
        super(Synth, self).__init__(**argd)
        polyphoniser = self.polyphoniser(**argd).activate()
        self.link((self, "inbox"), (polyphoniser, "inbox"), passthrough=1)

        for index, voice in enumerate(voiceGenerator()):
            voice = voice.activate()
            self.link((polyphoniser, "voice%i" % index), (voice, "inbox"))

    def main(self):
        """ Main loop """
        while 1:
            if not self.anyReady():
                self.pause()
            yield 1
