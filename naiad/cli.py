import argparse
import os
import sys
from contracts import contract
from naiad.bootstrap import bootstrap


@contract()
def get_working_directory(working_directory: str) -> str:
    # Confirm the working directory exists.
    if not os.path.isdir(working_directory):
        raise OSError('Working directory %s does not exist.' % working_directory)

    # Get the real path for readability.
    working_directory = os.path.realpath(working_directory)

    # Ensure a trailing slash for readability and path concatenation.
    working_directory.rstrip('/')
    working_directory += '/'

    return working_directory


def run():
    """
    Runs Naiad as a CLI application.
    """
    print('Welcome to Naiad.')
    parser = argparse.ArgumentParser(description='Runs Naiad.')
    parser.add_argument('-d', '--working-directory', help='The Naiad working directory. It defaults to the current working directory (%s).' % os.getcwd() , default=os.getcwd(), type=get_working_directory, dest='working_directory')
    try:
        working_directory = parser.parse_args().working_directory
        print('The Naiad working directory is %s.' % working_directory)
        naiad = bootstrap(working_directory)
        print('Running Naiad...')
        naiad.run()
    except Exception as e:
        sys.exit('Error: %s' % str(e))
