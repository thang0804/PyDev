from __future__ import absolute_import

import sys

if sys.version_info[0] >= 3:
    from tkinter.simpledialog import *  # type: ignore
else:
    from SimpleDialog import *  # type: ignore
