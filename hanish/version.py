# hanish.version
# Maintains version and package information for deployment.
#
# Author:   Benjamin Bengfort <benjamin@bengfort.com>
# Created:  Mon May 08 11:07:54 2017 -0400
#
# Copyright (C) 2016 Bengfort.com
# For license information, see LICENSE.txt
#
# ID: version.py [] benjamin@bengfort.com $

"""
Maintains version and package information for deployment.
"""

##########################################################################
## Module Info
##########################################################################

__version_info__ = {
    'major': 0,
    'minor': 1,
    'micro': 0,
    'releaselevel': 'final',
    'serial': 0,
}

##########################################################################
## Helper Functions
##########################################################################

def get_version(short=False):
    """
    Prints the version.
    """
    assert __version_info__['releaselevel'] in ('alpha', 'beta', 'final')
    vers = ["%(major)i.%(minor)i" % __version_info__, ]
    if __version_info__['micro']:
        vers.append(".%(micro)i" % __version_info__)
    if __version_info__['releaselevel'] != 'final' and not short:
        vers.append('%s%i' % (__version_info__['releaselevel'][0],
                              __version_info__['serial']))
    return ''.join(vers)
