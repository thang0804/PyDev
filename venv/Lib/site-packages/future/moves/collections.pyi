from __future__ import absolute_import
import sys

__future_module__ = True

from collections import *

if sys.version_info[0] == 2:
    from UserDict import UserDict
    from UserList import UserList
    from UserString import UserString

# if sys.version_info[0:2] == (2, 6):
#     from future.backports.misc import OrderedDict, Counter
#
# if sys.version_info < (3, 3):
#     from future.backports.misc import ChainMap, _count_elements
