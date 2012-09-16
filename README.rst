Bitcoins: Cryptocurrency for Humans
===================================

Bitcoins is an MIT licensed cryptocurrency library, written in Python, for human
beings.

Nothing is complicated when it's in Python. Not even cryptocurrencies.

::

    >>> bitcoins.get_difficulty()
    2694047.952955
    >>> bitcoins.get_block_count()
    198975
    >>> bitcoins.get_latest_hash()
    `00000000000000B8FCF51939B5FFDC13686D560061E46935A5671501938008F1`

For now, this library is only a wrapper to BlockExplorer's stats API. This might
change as the project matures.


Features
--------

Bitcoins can currently retrieve the following stats:

- Current difficulty as a multiple of the minimum difficulty (highest target)
- Number of blocks in the longest block chain (not including the genesis block)
- Latest block hash


Installation
------------

To install bitcoins, simply: ::

    $ pip install bitcoins

Or, if you have to: ::

    $ easy_install bitcoins

But, you probably shouldn't do that.
