from naiad_core import Configuration, Inventory

# Test whether the configuration file complies with its schema.
Configure('./example/naiad.configuration.json')

# Test whether the inventory file complies with its schema.
Inventory('./example/naiad.inventory.json')
