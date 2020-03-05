from __future__ import absolute_import

import sys

if sys.version_info[0] >= 3:
    from urllib.error import *
else:
    __future_module__ = True

    from urllib import ContentTooShortError
    from urllib2 import URLError, HTTPError
