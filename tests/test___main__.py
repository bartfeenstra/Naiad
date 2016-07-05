from subprocess import run
from unittest import TestCase


class TestMain(TestCase):
    def testExecution(self):
        working_directory = './example/'
        run(['python', '-m', 'naiad', working_directory])
