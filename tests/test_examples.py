from naiad.naiad_core import Configuration, Inventory
import os
from unittest import TestCase


class TestExamples(TestCase):
    """
    Tests whether the example JSON files comply with their schemas.
    """

    schemaDirectory = os.path.realpath('./schema') + '/'

    def testConfigurationExample(self):
        """
        Test whether the configuration file complies with its schema.
        """
        Configuration('./example/naiad.configuration.json')

    def testInventoryExample(self):
        """
        Test whether the inventory file complies with its schema.
        """
        Inventory('./example/naiad.inventory.json')
