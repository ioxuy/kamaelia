#!/usr/bin/python
#
# (C) 2006 British Broadcasting Corporation and Kamaelia Contributors(1)
#     All Rights Reserved.
#
# You may only modify and redistribute this under the terms of any of the
# following licenses(2): Mozilla Public License, V1.1, GNU General
# Public License, V2.0, GNU Lesser General Public License, V2.1
#
# (1) Kamaelia Contributors are listed in the AUTHORS file and at
#     http://kamaelia.sourceforge.net/AUTHORS - please extend this file,
#     not this notice.
# (2) Reproduced in the COPYING file, and at:
#     http://kamaelia.sourceforge.net/COPYING
# Under section 3.5 of the MPL, we are using this text since we deem the MPL
# notice inappropriate for this file. As per MPL/GPL/LGPL removal of this
# notice is prohibited.
#
# Please contact us via: kamaelia-list-owner@lists.sourceforge.net
# to discuss alternative licensing.
# -------------------------------------------------------------------------


import os

def isPythonFile(Path, File):
    FullEntry = os.path.join(Path, File)
    if os.path.isfile(FullEntry):
        if len(File) > 3:
            if File[-3:] == ".py":
                return True
    return False

def parseComponentLine(Line):
    components = [ x for x in Line[Line.find("(")+1:Line.rfind(")")].replace(" ", "").split(",") if x != ""]
    return components

def ComponentMeta(File, identifier="__kamaelia_components__"):
    F = open(File)
    contents = F.readlines()
    F.close()
    # find line beginning with __kamaelia_components__
    found = ""
    while len(contents)>0:
        line = contents.pop(0)
        line = line.strip()
        if identifier in line and line[0] != "#":
            if found != "":
                print "WARNING: 2 or more separate component lines(!) in "+str(File)
                break
            else:
                found+=line.replace("\n"," ")
                while ")" not in found:
                    if len(contents)==0:
                        print "WARNING: component line doesn't finish with a close bracket"
                    else:
                        line = contents.pop(0)
                        line = line.strip()
                        if line[0] != "#":
                            found += line
            
    found = found.strip()
    if found:
        meta = parseComponentLine(found)
    else:
        meta = []

    return meta

def SearchComponents(baseDirectory, Base, identifier="__kamaelia_components__"):
    Entries = os.listdir(baseDirectory)
    result = {}
    for Entry in Entries:
        if Entry == "Repository.py":
           continue
        FullEntry = os.path.join(baseDirectory, Entry)
        if isPythonFile(baseDirectory, Entry):

            meta = ComponentMeta(FullEntry, identifier)
            Entry = Entry[:-3]
            if meta:
                result[ tuple( Base+[ Entry ] ) ] = meta
        elif os.path.isdir(FullEntry):
            subtree = SearchComponents(FullEntry, Base+[Entry], identifier)
            result.update(subtree)
    return result

def SearchComponentsNested(baseDirectory, result, identifier="__kamaelia_components__"):
    Entries = os.listdir(baseDirectory)
    for Entry in Entries:
        if Entry == "Repository.py":
           continue
        FullEntry = os.path.join(baseDirectory, Entry)
        if isPythonFile(baseDirectory, Entry):

            meta = ComponentMeta(FullEntry, identifier)
            Entry = Entry[:-3]
            if meta:
                result[Entry] = meta
        elif os.path.isdir(FullEntry):
            if "Kamaelia/Support" != FullEntry[-16:]:
                try:
                    newresult = result[Entry]
                except KeyError:
                    newresult = {}
                    result[Entry] = newresult
                subtree = SearchComponentsNested(FullEntry, newresult, identifier)
    return result

def GetAllKamaeliaComponentsNested():
    import Kamaelia
    installbase = os.path.dirname(Kamaelia.__file__)
    base = { "Kamaelia" : {}}
    SearchComponentsNested(installbase, base["Kamaelia"] )
    return base

def GetAllKamaeliaComponents():
    import Kamaelia
    installbase = os.path.dirname(Kamaelia.__file__)
    return SearchComponents(installbase, ["Kamaelia"] )

def GetAllKamaeliaPrefabsNested():
    import Kamaelia
    installbase = os.path.dirname(Kamaelia.__file__)
    base = { "Kamaelia" : {}}
    SearchComponentsNested(installbase, base["Kamaelia"], "__kamaelia_prefabs__" )
    return base

def GetAllKamaeliaPrefabs():
    import Kamaelia
    installbase = os.path.dirname(Kamaelia.__file__)
    return SearchComponents(installbase, ["Kamaelia"], "__kamaelia_prefabs__" )

    
if __name__ == "__main__":
    import pprint
    pprint.pprint(GetAllKamaeliaComponents(),None,4)
    print
    print "*******************************************************************"
    print
    pprint.pprint(GetAllKamaeliaComponentsNested(),None,4)

# RELEASE: MH, MPS
