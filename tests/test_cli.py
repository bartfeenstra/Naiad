from naiad import cli
import os.path
from unittest import TestCase


class TestCli(TestCase):
    def testGetWorkingDirectoryWithExistingDirectory(self):
        overridden_working_directory = os.path.join(os.getcwd(), 'example')
        working_directory = cli.get_working_directory(overridden_working_directory)
        self.assertTrue(os.path.exists(working_directory))

    def testGetWorkingDirectoryWithNonExistentDirectory(self):
        with self.assertRaises(OSError):
            overridden_working_directory = os.path.join(os.getcwd(), 'foobar')
            cli.get_working_directory(overridden_working_directory)

