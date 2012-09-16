# -*- coding: utf-8 -*-

"""
bitcoins.api
~~~~~~~~~~~~

This module implements the Bitcoins API.

:copyright: (c) 2012 by Kenan Yildirim.
:license: MIT, see LICENSE for more details.

"""

import urllib
from .utils import blockexplorer


def get_difficulty():
    """Returns the current difficulty as a multiple of the minimum difficulty
    (highest target).
    """

    d = urllib.urlopen(blockexplorer('getdifficulty'))
    return float(d.read())


def get_block_count():
    """Returns the number of blocks in the longest block chain (not including
    the genesis block). Equivalent to Bitcoin's getblockcount.
    """

    d = urllib.urlopen(blockexplorer('getblockcount'))
    return int(d.read())
