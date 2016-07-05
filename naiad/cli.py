import os
import sys
from contracts import contract
from naiad.bootstrap import bootstrap


@contract
def get_working_directory() -> str:
    """
    Gets the current working directory.
    :rtype str
    """
    # There must be a single argument or none at all, but the first one is the script itself.
    if 1 > len(sys.argv) > 2:
        raise Exception(
            'This script accepts one argument which must be the working directory, but %d arguments were given.' % (
                len(sys.argv)))

    # If there is an argument, use it as the working directory.
    if len(sys.argv) == 2:
        working_directory = sys.argv[1]
    # Use the script's current working directory as the default.
    else:
        working_directory = os.getcwd()

    # Confirm the working directory exists.
    if not os.path.isdir(working_directory):
        raise Exception('Working directory %s does not exist.' % working_directory)

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
    try:
        working_directory = get_working_directory()
        print('The working directory is %s.' % working_directory)
        naiad = bootstrap(working_directory)
        print('Running Naiad...')
        naiad.run()
    except Exception as e:
        import sys
        sys.exit('Error: %s' % str(e))
