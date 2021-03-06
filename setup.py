#!/usr/bin/env python
# setup
# Setup script for installing hanish on a server.
#
# Author:   Benjamin Bengfort <benjamin@bengfort.com>
# Created:  Mon May 08 11:10:35 2017 -0400
#
# Copyright (C) 2016 Bengfort.com
# For license information, see LICENSE.txt
#
# ID: setup.py [] benjamin@bengfort.com $

"""
Setup script for installing hanish on a server.
See http://bbengfort.github.io/programmer/2016/01/20/packaging-with-pypi.html
"""

##########################################################################
## Imports
##########################################################################

import os
import re
import codecs

from setuptools import setup
from setuptools import find_packages

##########################################################################
## Package Information
##########################################################################

## Basic information
NAME         = "hanish"
DESCRIPTION  = "A slackbot that makes small talk about the weather."
AUTHOR       = "Benjamin Bengfort"
EMAIL        = "benjamin@bengfort.com"
MAINTAINER   = "Benjamin Bengfort"
LICENSE      = "MIT"
REPOSITORY   = "https://github.com/bbengfort/hanish"
PACKAGE      = "hanish"

## Define the keywords
KEYWORDS     = ('chatbot', 'slackbot', 'weather', 'api')

## Define the classifiers
## See https://pypi.python.org/pypi?%3Aaction=list_classifiers
CLASSIFIERS  = (
    'Development Status :: 3 - Alpha',
    'Environment :: Console',
    'Environment :: Web Environment',
    'Intended Audience :: Developers',
    'License :: OSI Approved :: MIT License',
    'Natural Language :: English',
    'Operating System :: OS Independent',
    'Programming Language :: Python',
    'Programming Language :: Python :: 2.7',
    'Topic :: Software Development',
    'Topic :: Communications :: Chat',
)

## Important Paths
PROJECT      = os.path.abspath(os.path.dirname(__file__))
REQUIRE_PATH = "requirements.txt"
VERSION_PATH = os.path.join(PACKAGE, "version.py")
PKG_DESCRIBE = "DESCRIPTION.rst"

## Directories to ignore in find_packages
EXCLUDES     = (
    "tests", "bin", "docs", "fixtures", "register", "notebooks", "examples",
)

##########################################################################
## Helper Functions
##########################################################################

def read(*parts):
    """
    Assume UTF-8 encoding and return the contents of the file located at the
    absolute path from the REPOSITORY joined with *parts.
    """
    with codecs.open(os.path.join(PROJECT, *parts), 'rb', 'utf-8') as f:
        return f.read()


def get_version(path=VERSION_PATH):
    """
    Reads the __init__.py defined in the VERSION_PATH to find the get_version
    function, and executes it to ensure that it is loaded correctly.
    """
    namespace = {}
    exec(read(path), namespace)
    return namespace['get_version'](short=True)


def get_requires(path=REQUIRE_PATH):
    """
    Yields a generator of requirements as defined by the REQUIRE_PATH which
    should point to a requirements.txt output by `pip freeze`.
    """
    for line in read(path).splitlines():
        line = line.strip()
        if line and not line.startswith('#'):
            yield line

##########################################################################
## Define the configuration
##########################################################################

config = {
    "name": NAME,
    "version": get_version(),
    "description": DESCRIPTION,
    "long_description": read(PKG_DESCRIBE),
    "license": LICENSE,
    "author": AUTHOR,
    "author_email": EMAIL,
    "maintainer": MAINTAINER,
    "maintainer_email": EMAIL,
    "url": REPOSITORY,
    "download_url": "{}/tarball/v{}".format(REPOSITORY, get_version()),
    "packages": find_packages(where=PROJECT, exclude=EXCLUDES),
    "install_requires": list(get_requires()),
    "classifiers": CLASSIFIERS,
    "keywords": KEYWORDS,
    "zip_safe": False,
    "scripts": ["hanishbot.py"],
}

##########################################################################
## Run setup script
##########################################################################

if __name__ == '__main__':
    setup(**config)
