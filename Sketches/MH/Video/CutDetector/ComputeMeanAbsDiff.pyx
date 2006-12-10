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
#

cdef extern from "ComputeMAD.c":
    cdef double ComputeMAD( unsigned char *prev, unsigned char *curr, int size)


cdef extern from "Python.h": 
    object PyString_FromStringAndSize(char *, int)
    cdef char* PyString_AsString(object)


def ComputeMeanAbsDiff(ydata1,ydata2):
    cdef unsigned char *y1
    cdef unsigned char *y2

    y1 = <unsigned char *>PyString_AsString(ydata1)
    y2 = <unsigned char *>PyString_AsString(ydata2)

    return ComputeMAD(y1, y2, len(ydata1))
