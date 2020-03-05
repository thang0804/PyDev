from __future__ import absolute_import
import sys

if sys.version_info[0] >= 3:
    from html.entities import *
else:
    __future_module__ = True
    from htmlentitydefs import *
