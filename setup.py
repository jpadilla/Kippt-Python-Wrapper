#!/usr/bin/env python

import os
import sys

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

if sys.argv[-1] == 'publish':
    os.system('python setup.py sdist upload')
    sys.exit()

os.environ['PYTHONDONTWRITEBYTECODE'] = '1'

setup(
    name='kippt',
    version="1.0.2",
    description='Kippt.com API wrapper for Python',
    long_description=open('README').read(),
    author='TJ (Thomas) Biddle',
    author_email='me@ThomasBiddle.com',
    url='https://github.com/thomasbiddle/Kippt-Python-Wrapper',
    packages=['kippt',],
    package_data={'': ['LICENSE']},
    install_requires=['requests'],
    include_package_data=True,
    license='wtfpl',
)

del os.environ['PYTHONDONTWRITEBYTECODE']
