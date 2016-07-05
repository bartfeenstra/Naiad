import abc
from contracts import contract
from jsonschema import RefResolver, validate
import json
import os
import importlib
import re
import sys


class Configuration:
    @contract
    def __init__(self, configuration_file_path: str):
        """
        :type configuration_file_path: str
        """
        schema_directory = os.path.realpath('./schema') + '/'
        configuration_schema_file_path = os.path.join(schema_directory, 'naiad.configuration.schema.json')
        configuration_schema_reference_resolver = RefResolver('file://' + schema_directory,
                                                              configuration_schema_file_path)
        configuration = json.load(open(configuration_file_path, 'r'))
        validate(configuration, json.load(open(configuration_schema_file_path, 'r')),
                 resolver=configuration_schema_reference_resolver)

        self._configuration = configuration


class Inventory:
    @contract
    def __init__(self, inventory_file_path: str):
        """
        :type inventory_file_path: str
        """
        schema_directory = os.path.realpath('./schema') + '/'
        inventory_schema_file_path = os.path.join(schema_directory, 'naiad.inventory.schema.json')
        inventory_schema_reference_resolver = RefResolver('file://' + schema_directory, inventory_schema_file_path)
        inventory = json.load(open(inventory_file_path, 'r'))
        validate(inventory, json.load(open(inventory_schema_file_path, 'r')),
                 resolver=inventory_schema_reference_resolver)

        self._inventory = inventory


class Controller:
    @contract
    def __init__(self, configuration: object):
        """
        :type configuration: object
        """
        self._configuration = configuration

    @classmethod
    @contract
    def create_instance(cls, configuration: object):
        """
        :type configuration: object
        :rtype naiad.core.Controller
        """
        return cls(configuration)


class Naiad:
    @contract
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
        pass

    @staticmethod
    @contract
    def _controller_get(definition: str, configuration: object) -> Controller:
        """
        :type definition: str
        :type configuration: object
        :rtype naiad.core.Controller
        """
        if not re.fullmatch('^[^#]+#[^#]+$', definition):
            raise ValueError(
                'A controller definition must be a module name and aclass name, separated by a hash/pound, but "%s" was given. Example: foo.bar#Baz' % definition)
        module_name, class_name = definition.split('#', 1)
        module = sys.modules[module_name]
        importlib.import_module(module_name)
        controller_class = getattr(module, class_name)

        return controller_class.create_instance(configuration)


class MoistureFeedController(Controller):
    @abc.abstractmethod
    @contract
    def feed(self, volume: int):
        """
        :type volume: int
        :rtype None
        """
        pass
