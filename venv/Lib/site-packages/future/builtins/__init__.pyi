import sys

from future.builtins.iterators import filter as filter
from future.builtins.iterators import map as map
from future.builtins.iterators import zip as zip

from future.builtins.misc import ascii as asci
from future.builtins.misc import chr as chr
from future.builtins.misc import hex as hex
from future.builtins.misc import input as input
from future.builtins.misc import isinstance as isinstance
from future.builtins.misc import next as next
from future.builtins.misc import oct as oct
from future.builtins.misc import pow as pow
from future.builtins.misc import round as round
from future.builtins.misc import super as super
from future.builtins.misc import max as max
from future.builtins.misc import min as min


if sys.version_info[0] >= 3:
    import builtins
    bytes = builtins.bytes
    dict = builtins.dict
    int = builtins.int
    list = builtins.list
    object = builtins.object
    range = builtins.range
    str = builtins.str
    __all__ = []
else:
    from future.types import (newbytes as bytes,
                              newdict as dict,
                              newint as int,
                              newlist as list,
                              newobject as object,
                              newrange as range,
                              newstr as str)


if not sys.version_info[0] >= 3:
    # We only import names that shadow the builtins on Py2. No other namespace
    # pollution on Py2.

    # Only shadow builtins on Py2; no new names
    __all__ = ['filter', 'map', 'zip',
               'ascii', 'chr', 'hex', 'input', 'next', 'oct', 'open', 'pow',
               'round', 'super',
               'bytes', 'dict', 'int', 'list', 'object', 'range', 'str', 'max', 'min'
              ]

else:
    # No namespace pollution on Py3
    __all__ = []
