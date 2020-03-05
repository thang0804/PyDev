from __future__ import absolute_import
from typing import AnyStr

import sys
__future_module__ = True

if sys.version_info[0] >= 3:
    from html import *
else:
    # cgi.escape isn't good enough for the single Py3.3 html test to pass.
    # Define it inline here instead. From the Py3.4 stdlib. Note that the
    # html.escape() function from the Py3.3 stdlib is not suitable for use on
    # Py2.x.
    """
    General functions for HTML manipulation.
    """

    def escape(s: AnyStr, quote=True) -> AnyStr: ...

    __all__ = ['escape']
