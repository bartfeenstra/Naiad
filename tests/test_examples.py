import json
from jsonschema import RefResolver, validate
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
        configurationSchemaFilePath = self.schemaDirectory + 'naiad.configuration.schema.json'
        configurationSchemaReferenceResolver = RefResolver('file://' + self.schemaDirectory, configurationSchemaFilePath)
        validate(json.load(open('./example/naiad.configuration.json', 'r')),
                 json.load(open(configurationSchemaFilePath, 'r')), resolver=configurationSchemaReferenceResolver)

    def testInventoryExample(self):
        """
        Test whether the inventory file complies with its schema.
        """
        inventorySchemaFilePath = self.schemaDirectory + 'naiad.inventory.schema.json'
        inventorySchemaReferenceResolver = RefResolver('file://' + self.schemaDirectory, inventorySchemaFilePath)
        validate(json.load(open('./example/naiad.inventory.json', 'r')),
                 json.load(open(inventorySchemaFilePath, 'r')), resolver=inventorySchemaReferenceResolver)
