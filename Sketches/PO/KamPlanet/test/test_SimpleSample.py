from Axon.Ipc import producerFinished
import kamtest.KamTestCase as KamTestCase
from SimpleSample import SimpleComponent

class SimpleSampleTestCase(KamTestCase.KamTestCase):
    def setUp(self):
        self.simpleSample = SimpleComponent()
        self.initializeSystem(self.simpleSample)
        
    def testForwardsNumbers(self):
        self.put(5, 'numbers')
        self.put(6, 'numbers')
        self.putYield(10)
        self.put(producerFinished(), 'control')
        self.assertStopping()
        self.assertEquals('5', self.get('outbox'))
        self.assertEquals('6', self.get('outbox'))
        self.assertOutboxEmpty('outbox')
        self.assertTrue(isinstance(self.get('signal'), producerFinished))
        self.assertOutboxEmpty('signal')

def suite():
    return KamTestCase.makeSuite(
            SimpleSampleTestCase.getTestCase()
        )
        
if __name__ == '__main__':
    KamTestCase.main(defaultTest='suite')