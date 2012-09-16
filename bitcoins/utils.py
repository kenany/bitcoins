from . import __version__

BLOCKEXPLORER_URL = 'https://blockexplorer.com/q/'


def blockexplorer(*suffix):
    """Returns url for BLOCKEXPLORER resource."""
    return BLOCKEXPLORER_URL + '/'.join(suffix)
