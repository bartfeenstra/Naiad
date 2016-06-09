import abc
from jsonschema import RefResolver, validate
import json
import os
import importlib
import re


class Naiad:
    def __init__(self, configuration: Configuration, inventory: Inventory):
        """
        :type configuration: Configuration
        :type inventory: Inventory

        """
        self._configuration = configuration
        self._inventory = inventory

    def run(self):
        # Parse the inventory + config and create a list of actions to take. This will support any future actions other
        # than moisture. Then create an infinite loop that goes over the actions every second. For every action,
        # check if it must be executed. If so, do so.



class Configuration:
    def __init__(self, configuration_file_path: str):
        """
        :type configuration_file_path: str

        """
        schema_directory = os.path.realpath('./schema') + '/'
        configuration_schema_file_path = schema_directory + 'naiad.configuration.schema.json'
        configuration_schema_reference_resolver = RefResolver('file://' + schema_directory,
                                                              configuration_schema_file_path)
        configuration = json.load(open(configuration_file_path, 'r'))
        validate(configuration, json.load(open(configuration_schema_file_path, 'r')),
                 resolver=configuration_schema_reference_resolver)

        self._configuration = configuration


class Inventory:
    def __init__(self, inventory_file_path: str):
        """
        :type inventory_file_path: str

        """
        schema_directory = os.path.realpath('./schema') + '/'
        inventory_schema_file_path = schema_directory + 'naiad.inventory.schema.json'
        inventory_schema_reference_resolver = RefResolver('file://' + schema_directory, inventory_schema_file_path)
        inventory = json.load(open(inventory_file_path, 'r'))
        validate(inventory, json.load(open(inventory_schema_file_path, 'r')),
                 resolver=inventory_schema_reference_resolver)

        self._inventory = inventory


class Controller:
    def __init__(self, configuration: object):
        """
        :type configuration: object

        """
        self._configuration = configuration

    @classmethod
    def create_instance(cls, configuration: object):
        """
        :type configuration: object
        :rtype Controller
        """
        return cls(configuration)


class MoistureFeedController(Controller):
    @abc.abstractmethod
    def feed(self, volume: int):
        """
        :type volume: int
        :rtype None
        """
        pass

def controller_get(definition: str) -> Controller:
    """
    :type definition: str
    :rtype Controller
    """
    re.fullmatch('', definition)
    importlib.import_module(name, package)
    return False