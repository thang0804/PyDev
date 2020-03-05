from __future__ import absolute_import
import sys

if sys.version_info[0] >= 3:
    from http.cookies import *
else:
    __future_module__ = True
    from Cookie import *
    from Cookie import Morsel    # left out of __all__ on Py2.7!
