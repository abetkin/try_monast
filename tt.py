from twisted.internet import reactor
from twisted.trial.unittest import TestCase



from monast import Monast





class Interact(TestCase):

    d = {}

    @classmethod
    def setUpClass(cls):
        cls.monast = Monast('/etc/monast.conf')
        super(Interact, cls).setUpClass()

    def test_1(self):
        session = {}
        action = {
            'server': ['Server1'],
            'to': ['600'],
            'from': ['SIP/caller'],
            'type': ['dial'],
        }
        self.monast.clientAction_Originate(self, session, action)

    def test_2(self):
        self.d['a'] = self.d['a'] + 1

    def test_3(self):
        self.assertEqual(self.d['a'], 2)
