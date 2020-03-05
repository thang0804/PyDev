from __future__ import absolute_import
import sys
__future_module__ = True

if sys.version_info[0] >= 3:
    from html.parser import *
else:
    from HTMLParser import *
