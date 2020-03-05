from __future__ import absolute_import

import sys

if sys.version_info[0] >= 3:
    from tkinter.constants import *  # type: ignore
else:
    from Tkconstants import *  # type: ignore
