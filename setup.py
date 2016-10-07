# -*- coding: utf-8 -*-

from setuptools import setup, find_packages


with open('README.rst') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

setup(
    name='RoboteQ-Python',
    version='0.0.1',
    description='Python Wrapper for RoboteQ Motor Driver Serial APIs',
    long_description=readme,
    author='Deval Shah',
    author_email='deval.maker@gmail.com',
    url='https://github.com/deval-maker/RoboteQ-Python/',
    license=license,
    packages=find_packages(exclude=('tests', 'docs'))
)

