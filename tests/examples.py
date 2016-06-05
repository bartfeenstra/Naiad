import json
from jsonschema import RefResolver, validate
import os

schemaDirectory = os.path.realpath('./schema') + '/'

# Test whether the configuration file complies with its schema.
configurationSchemaFilePath = schemaDirectory + 'naiad.configuration.schema.json'
configurationSchemaReferenceResolver = RefResolver('file://' + schemaDirectory, configurationSchemaFilePath)
validate(json.load(open('./example/naiad.configuration.json', 'r')),
         json.load(open(configurationSchemaFilePath, 'r')), resolver=configurationSchemaReferenceResolver)

# Test whether the inventory file complies with its schema.
inventorySchemaFilePath = schemaDirectory + 'naiad.inventory.schema.json'
inventorySchemaReferenceResolver = RefResolver('file://' + schemaDirectory, inventorySchemaFilePath)
validate(json.load(open('./example/naiad.inventory.json', 'r')),
         json.load(open(inventorySchemaFilePath, 'r')), resolver=inventorySchemaReferenceResolver)
