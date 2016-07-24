from contracts.interface import ContractNotRespected
from naiad.example import ExampleMoistureFeedController
from unittest import TestCase


class TestExampleMoistureFeedController(TestCase):
    def testFeedWithValidVolume(self):
        controller = ExampleMoistureFeedController()
        controller.feed(0.01)

    def testFeedWithInvalidVolume(self):
        controller = ExampleMoistureFeedController()
        with self.assertRaises(ContractNotRespected):
            controller.feed('foo')
