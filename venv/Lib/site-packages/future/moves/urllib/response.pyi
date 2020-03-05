import sys

if sys.version_info[0] >= 3:
    from urllib.response import *
else:
    __future_module__ = True
    from urllib import (addbase,
                        addclosehook,
                        addinfo,
                        addinfourl)
