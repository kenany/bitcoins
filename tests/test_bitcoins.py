#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import os
sys.path.insert(0, os.path.abspath('..'))
import bitcoins
import unittest
import urllib


class BitcoinsTestSuite(unittest.TestCase):

    _multiprocess_can_split_ = True

    def test_get_difficulty(self):
        d = urllib.urlopen('https://blockexplorer.com/q/getdifficulty')
        assert bitcoins.get_difficulty() == float(d.read())

if __name__ == '__main__':
    unittest.main()
