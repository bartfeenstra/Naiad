import os
import sys
from .naiad_core import Configuration, Inventory, Naiad


def get_working_directory():
    """
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
        if not os.path.exists(working_directory):
            raise Exception('Working directory %s does not exist.' % working_directory)
    # Use the script's current working directory as the default.
    else:
        working_directory = os.getcwd()

    return working_directory + '/'


def bootstrap(working_directory: str):
    """
    :type working_directory: str
    :rtype Naiad

    """
    configuration_file_path = working_directory + 'naiad.configuration.json'
    if not os.path.exists(configuration_file_path):
        raise Exception(
            'Naiad working directory %s does not contain the required configuration file %s.' % (working_directory,
                                                                                                 configuration_file_path))
    configuration = Configuration(configuration_file_path)
    inventory_file_path = working_directory + 'naiad.inventory.json'
    if not os.path.exists(inventory_file_path):
        raise Exception(
            'Naiad working directory %s does not contain the required inventory file %s.' % (working_directory,
                                                                                             inventory_file_path))
    inventory = Inventory(inventory_file_path)

    return Naiad(configuration, inventory)


naiad = bootstrap(get_working_directory())
naiad.run()
