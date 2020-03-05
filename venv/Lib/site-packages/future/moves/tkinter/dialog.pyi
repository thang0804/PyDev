from __future__ import absolute_import

import sys

if sys.version_info[0] >= 3:
    from tkinter.dialog import *  # type: ignore
else:
    from Dialog import *  # type: ignore
