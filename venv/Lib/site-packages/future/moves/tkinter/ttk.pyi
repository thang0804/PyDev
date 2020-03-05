from __future__ import absolute_import

import sys

if sys.version_info[0] >= 3:
    from tkinter.ttk import *
else:
    from ttk import *  # type: ignore
