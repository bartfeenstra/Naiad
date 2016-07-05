from distutils.core import setup

setup_parameters = dict(
    name='Naiad',
    packages=['naiad'],
    entry_points={
        'console_scripts': [
            'naiad = naiad.cli:run'
        ]
    },
)
setup(**setup_parameters)
