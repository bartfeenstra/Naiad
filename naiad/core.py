import abc
from contracts import contract
from jsonschema import RefResolver, validate
import json
import os
import importlib
import re
import sys
import time
from threading import Thread
from typing import List


class Controller:
    @contract
    def __init__(self, configuration: object = {}):
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


class MoistureFeedController(Controller):
    @abc.abstractmethod
    @contract
    def feed(self, volume: float):
        """
        :type volume: float
        :rtype None
        """
        pass


class Task:
    @abc.abstractmethod
    def execute(self):
        """
        Executes the task.
        """
        pass


class MoistureFeedTask(Task):
    @contract
    def __init__(self, interval: int, controller: MoistureFeedController, volume: float):
        """
        :type interval: int
        :param interval: The task's execution interval in seconds.
        :type controller: naiad.core.MoistureFeedController
        :type volume: float
        :param volume: The volume to feed in liters.
        """
        self._interval = interval
        self._controller = controller
        self._volume = volume

    def execute(self):
        while True:
            self._controller.feed(self._volume)
            time.sleep(self._interval)


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

    @contract
    def get_tasks(self) -> List[Task]:
        """
        :rtype: naiad.core.Task[]
        """
        tasks = []
        for target in self._inventory['inventory']:
            controller = self._get_controller(target['care']['moisture']['feed']['controller']['class'], target['care']['moisture']['feed']['controller']['configuration'])
            tasks.append(MoistureFeedTask(target['care']['moisture']['feed']['schedule']['interval'], controller, target['care']['moisture']['feed']['schedule']['volume']))

        return tasks


    @staticmethod
    @contract
    def _get_controller(definition: str, configuration: object) -> Controller:
        """
        :type definition: str
        :type configuration: object
        :rtype naiad.core.Controller
        """
        if not re.fullmatch('^[^#]+#[^#]+$', definition):
            raise ValueError(
                'A controller definition must be a module name and aclass name, separated by a hash/pound, but "%s" was given. Example: foo.bar#Baz' % definition)
        module_name, class_name = definition.split('#', 1)
        importlib.import_module(module_name)
        module = sys.modules[module_name]
        controller_class = getattr(module, class_name)

        return controller_class.create_instance(configuration)


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
        """
        Runs Naiad.
        """
        threads = []
        for task in self._inventory.get_tasks():
            thread = Thread(None, task.execute)
            thread.start()
            threads.append(thread)
        for thread in threads:
            thread.join()
