from naiad import cli
import os.path
import sys
from unittest import TestCase


class TestCli(TestCase):
    def testGetWorkingDirectoryWithDefault(self):
        working_directory = cli.get_working_directory()
        self.assertTrue(os.path.exists(working_directory))

    def testGetWorkingDirectoryWithShellArgument(self):
        argv = sys.argv
        try:
            overridden_working_directory = os.path.realpath('./example/') + '/'
            sys.argv = ['script_name', overridden_working_directory]
            working_directory = cli.get_working_directory()
        finally:
            # Restore sys.argv so the changes do not leak to other tests.
            sys.argv = argv
        self.assertEqual(working_directory, overridden_working_directory)

