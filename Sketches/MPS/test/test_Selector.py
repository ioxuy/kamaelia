#!/usr/bin/python

import unittest

import sys; sys.path.append("../")
from Selector import Selector

import Axon

class SmokeTests_Selector(unittest.TestCase):
    def test_SmokeTest(self):
        """__init__ - Called with no arguments succeeds"""
        S = Selector()
        self.assert_(isinstance(S, Axon.Component.component))

    def test_RunsForever(self):
        """main - Run with no messages, keeps running"""
        S = Selector()
        S.activate()
        for i in xrange(1,100):
            try:
                S.next()
            except StopIteration:
                self.fail("Component should run until told to stop. Failed on iteration: "+str(i))

    def test_PausesUntilFirstMessage(self):
        """main - Before we recieve any messages telling us what to watch for, the system should pause and yield"""
        S = Selector()
        S.activate()
        V = S.next()
        self.assert_(S._isRunnable() is not True)

if __name__=="__main__":
    unittest.main()
