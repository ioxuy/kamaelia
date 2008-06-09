#!/usr/bin/env python

from likefile import likeFile, schedulerThread
from Kamaelia.Protocol.HTTP.HTTPClient import SimpleHTTPClient

# the setup
schedulerThread(slowmo = 0.01).start()
p = likeFile(SimpleHTTPClient())

p.put("http://google.com", "inbox")
p.put("http://slashdot.org", "inbox")
p.put("http://whatismyip.org", "inbox")
google = p.get("outbox", True) # block until page recieved
slashdot = p.get("outbox", True) # block until page recieved
whatismyip = p.get("outbox", True) # block until page recieved
print "google is", len(google), "bytes long, and slashdot is", len(slashdot), "bytes long. Also, our IP address is:", whatismyip