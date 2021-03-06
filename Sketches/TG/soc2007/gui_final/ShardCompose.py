#!/usr/bin/python
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

import Axon
from Tree import Tree

from ConnectorShardsGUI import ConnectorShardsGUI
from ImportShardsGUI import ImportShardsGUI
from CodeDisplay import TextOutputGUI

from Kamaelia.UI.Pygame.Button import Button
from Kamaelia.Chassis.Graphline import Graphline

    
class CoreLogic(Axon.Component.component):
    """
    This is the central dispatch point for the GUI, handling addition
    and editing of nodes and connecting the node tree to the shard
    and display dialogue boxes
    """
    
    def __init__(self):
        self.Outboxes['popup'] = 'selector signals to connector shards gui'
        self.Outboxes['textbox'] = 'generated code to text display'
        super(CoreLogic, self).__init__()
    
    def main(self):
        selected = None
        while 1:
            while self.dataReady("inbox"):
                command = self.recv("inbox")
                
                if command[0] == "SELECT":
                    # select msg is ['select', 'node', shardgen obj.]
                    self.send(['select', 'node', command[1]], 'popup')
                    selected = command[1]
                
                if command[0] == "ADD":
                    # add msg is ['ADD', shardgen object, name]
                    self.send(["add", command[1], command[2], selected ],"outbox")
                    self.send(["select", command[1]],"outbox")
                
                if command[0] == "GEN":
                    # generate code, no parameters needed
                    self.send('generate', 'outbox')
                
                if command[0] == 'disp':
                    # send given text to text display
                    self.send(['text', command[1]], 'textbox')
                
                if command[0] == "DEL":
                    if selected:
                        nodeId = nodeId + 1
                        self.send(["del", "node", selected ],"outbox")
                
                if command[0] == "RELABEL":
                    if selected:
                        self.send(["relabel", selected, command[1]],"outbox")
                        self.send(["select", selected ],"outbox")
            
            yield 1

# import shard classes
from Shard import shard, docShard
from LoopShard import whileShard, forShard
from ComponentShard import componentShard
from ModuleShard import moduleShard
from BranchShard import switchShard
from ClassShard import classShard
from FuncAppShard import funcAppShard
from FunctionShard import functionShard, importFunctionShard
from InitShard import initShard
from PygameComponentShard import pygameComponentShard

items = [shard, docShard, forShard, switchShard, whileShard, componentShard,
              moduleShard, classShard, funcAppShard, functionShard, initShard,
              importFunctionShard, pygameComponentShard]

Graphline(
CLEAR = Button(caption="Clear", msg=["del", "all"], position=(0,690),size=(64,32)),
GEN= Button(caption="Generate", msg=["GEN"], position=(70,690),size=(64,32)),
DEL= Button(caption="Del Node", msg=["DEL"], position=(140,690),size=(64,32)),
RELABEL= Button(caption="Relabel Node", msg=["RELABEL"], position=(210,690),size=(94,32)),
CORELOGIC = CoreLogic(),
TOPOLOGY = Tree(),
IMP = ImportShardsGUI('/home/ert/kamaelia-trunk'),
CON = ConnectorShardsGUI(items),
DISP = TextOutputGUI('Generated Code'),
linkages = {
    ("CLEAR", "outbox"): ("TOPOLOGY","inbox"),
    ("TOPOLOGY","outbox"): ("CORELOGIC", "inbox"),
    ("GEN","outbox"): ("CORELOGIC", "inbox"),
    ("DEL","outbox"): ("CORELOGIC", "inbox"),
    ("RELABEL","outbox"): ("CORELOGIC", "inbox"),
    ("CORELOGIC","outbox"): ("TOPOLOGY", "inbox"),
    ("IMP","outbox"): ("CORELOGIC", "inbox"),
    ("CON","outbox"): ("CORELOGIC", "inbox"),
    ("CORELOGIC","popup"): ("CON", "inbox"),
    ("CORELOGIC", 'textbox'): ('DISP', 'inbox')
}
).run()