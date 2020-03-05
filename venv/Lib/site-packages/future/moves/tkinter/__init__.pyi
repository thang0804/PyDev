from __future__ import absolute_import
import sys
__future_module__ = True

if not sys.version_info[0] >= 3:
    from Tkinter import *
    from Tkinter import (_cnfmerge, _default_root, _flatten,
                          _support_default_root, _test,
                         _tkinter, _setit)

    try: # >= 2.7.4
        from Tkinter import (_join)
    except ImportError:
        pass

    try: # >= 2.7.4
        from Tkinter import (_stringify)
    except ImportError:
        pass

    try: # >= 2.7.9
        from Tkinter import (_splitdict)
    except ImportError:
        pass

else:
    from tkinter import *
