from naiad.core import Configuration, Controller, Inventory, MoistureFeedTask, MoistureFeedController, Task
from unittest import TestCase
from unittest.mock import Mock
from jsonschema.exceptions import ValidationError


class TestConfiguration(TestCase):
    def test__Init__WithValidConfigurationFile(self):
        Configuration('./example/naiad.configuration.json')

    def test__Init__WithInvalidConfigurationFile(self):
        with self.assertRaises(ValidationError):
            Configuration('./example/naiad.inventory.json')

    def test__Init__WithNonExistentConfigurationFile(self):
        with self.assertRaises(FileNotFoundError):
            Configuration('foo')


class TestInventory(TestCase):
    def test__Init__WithValidInventoryFile(self):
        Inventory('./example/naiad.inventory.json')

    def test__Init__WithInvalidInventoryFile(self):
        with self.assertRaises(ValidationError):
            Inventory('./example/naiad.configuration.json')

    def test__Init__WithNonExistentInventoryFile(self):
        with self.assertRaises(FileNotFoundError):
            Inventory('foo')

    def testGetController(self):
        definition = 'test_core#TestNaiadDummyController'
        configuration = dict()
        controller = Inventory._get_controller(definition, configuration)
        self.assertIsInstance(controller, Controller)

    def testGetTasks(self):
        inventory = Inventory('./example/naiad.inventory.json')
        tasks = inventory.get_tasks()
        self.assertIsInstance(tasks, list)
        for task in tasks:
            self.assertIsInstance(task, Task)


class TestController(TestCase):
    def testCreateInstance(self):
        configuration = dict()
        controller = Controller(configuration)
        self.assertIsInstance(controller, Controller)


class TestMoistureFeedTask(TestCase):
    def test__Init__(self):
        interval = 7
        controller = Mock(spec=MoistureFeedController)
        volume = 0.123
        task = MoistureFeedTask(interval, controller, volume)
        self.assertIsInstance(task, MoistureFeedTask)


class TestNaiad(TestCase):
    pass


class TestNaiadDummyController(Controller):
    pass
