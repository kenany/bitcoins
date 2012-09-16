Bitcoins: Cryptocurrency for Humans
===================================

Bitcoins is an MIT licensed cryptocurrency library, written in Python, for human
beings.

Nothing is complicated when it's in Python. Not even cryptocurrencies.

::

    >>> bitcoins.get_difficulty()
    2694047.952955

For now, this library is only a wrapper to BlockExplorer's stats API. This might
change as the project matures.

Features
--------

- Getting the current difficulty as a multiple of the minimum difficulty
  (highest target)


Installation
------------

To install bitcoins, simply: ::

    $ pip install bitcoins

Or, if you have to: ::

    $ easy_install bitcoins

But, you probably shouldn't do that.
