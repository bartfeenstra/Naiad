from contracts.interface import ContractNotRespected
from naiad.bootstrap import bootstrap
from naiad.core import Naiad
from unittest import TestCase


class TestBootstrap(TestCase):
    def testCall(self):
        working_directory = './example/'
        naiad = bootstrap(working_directory)
        self.assertIsInstance(naiad, Naiad)

    def testCallWithInt(self):
        with self.assertRaises(ContractNotRespected):
            working_directory = 7
            bootstrap(working_directory)
