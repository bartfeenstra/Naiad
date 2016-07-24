from subprocess import run, TimeoutExpired
from unittest import TestCase


class TestMain(TestCase):
    def testExecution(self):
        working_directory = './example/'
        with self.assertRaises(TimeoutExpired):
            run(['python', '-m', 'naiad', '-d', working_directory], timeout=1)
