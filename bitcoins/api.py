# -*- coding: utf-8 -*-

"""
bitcoins.api
~~~~~~~~~~~~

This module implements the Bitcoins API.

:copyright: (c) 2012 by Kenan Yildirim.
:license: MIT, see LICENSE for more details.

"""

import urllib


def get_difficulty():
    """Retrieves the current difficulty as a multiple of the minimum difficulty
    (highest target).
    """

    d = urllib.urlopen('https://blockexplorer.com/q/getdifficulty')
    return float(d.read())
