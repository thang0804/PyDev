import sys
from typing import List

if sys.version_info[0] < 3:
    import itertools
    filter = itertools.ifilter
    map = itertools.imap
    from future.types import newrange as range
    zip = itertools.izip
    __all__ = ['filter', 'map', 'range', 'zip']
else:
    import builtins
    filter = builtins.filter
    map = builtins.map
    range = builtins.range
    zip = builtins.zip
    __all__ = []  # type: List[str]
