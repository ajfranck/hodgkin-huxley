from setuptools import setup, find_packages

setup(
    name='hodgkin-huxley',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        'numpy',
        'scipy',
        'matplotlib',
    ],
    author='Andy Franck',
    author_email='franck@oxy.edu',
    description=
    'An investigation of dynamics of nerve impulses usign simulations of the Hodgkin-Huxley model.'
)
