from setuptools import setup

setup(
    name='ohmyrepos',
    version='0.1.0',
    packages=['ohmyrepos'],
    entry_points={
        'console_scripts': [
            'pull=ohmyrepos.__main__:main'
        ]
    })
