from __future__ import absolute_import

import sys

if sys.version_info[0] >= 3:
    from dbm.gnu import *
else:
    __future_module__ = True
    from gdbm import *
