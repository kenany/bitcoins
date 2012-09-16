#!/usr/bin/env python

import os
import sys
import bitcoins

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

if sys.argv[-1] == 'publish':
    os.system('python setup.py sdist upload')
    sys.exit()

os.environ['PYTHONDONTWRITEBYTECODE'] = '1'

packages = ['bitcoins']

requires = []

setup(
    name='bitcoins',
    version=bitcoins.__version__,
    description='Python Bitcoins for Humans.',
    long_description=open('README.rst').read(),
    author='Kenan Yildirim',
    author_email='kenan@kenany.me',
    url='https://github.com/KenanY/bitcoins',
    packages=packages,
    install_requires=requires,
    license=open('LICENSE').read(),
    classifiers=(
        'Development Status :: 1 - Planning',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
    ),
)

del os.environ['PYTHONDONTWRITEBYTECODE']
