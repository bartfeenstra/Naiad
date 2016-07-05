from naiad.core import Configuration, Controller, Inventory, Naiad
from unittest import TestCase
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


class TestController(TestCase):
    def testCreateInstance(self):
        configuration = dict()
        controller = Controller(configuration)
        self.assertIsInstance(controller, Controller)


class TestNaiad(TestCase):
    def testGetController(self):
        definition = 'test_core#TestNaiadDummyController'
        configuration = dict()
        controller = Naiad._controller_get(definition, configuration)
        self.assertIsInstance(controller, Controller)


class TestNaiadDummyController(Controller):
    pass
