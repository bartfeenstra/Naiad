from contracts import contract
from naiad.core import Configuration, Inventory, Naiad
import os


@contract
def bootstrap(working_directory: str) -> Naiad:
    """
    Bootstraps Naiad.
    :type working_directory: str
    :rtype naiad.core.Naiad
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