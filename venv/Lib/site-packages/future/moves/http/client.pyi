import sys

if sys.version_info[0] >= 3:
    from http.client import *
else:
    from httplib import *
    from httplib import HTTPMessage
    __future_module__ = True
