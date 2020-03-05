from __future__ import absolute_import

import sys

if sys.version_info[0] >= 3:
    from tkinter.filedialog import *  # type: ignore
else:
    from FileDialog import *  # type: ignore

