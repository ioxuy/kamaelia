#!/usr/bin/env python
#
# (C) 2008 British Broadcasting Corporation and Kamaelia Contributors(1)
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

from distutils.core import setup
import py2exe

setup(name = "Kamaelia-Jam",
      version = "0.1a1",
      description = "Kamaelia Jam - a multi-user networked music sequencer",
      author = "Joe Turner & Kamaelia Contributors",
      author_email = "ms_@users.sourceforge.net",
      url = "http://kamaelia.sourceforge.net/KamaeliaJam",
      license = "Copyright (c)2008 BBC & Kamaelia Contributors, All Rights Reserved. Use allowed under MPL 1.1, GPL 2.0, LGPL 2.1",
      windows=['jam']
     )
