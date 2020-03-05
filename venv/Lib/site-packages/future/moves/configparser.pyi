from __future__ import absolute_import

import sys

if sys.version_info[0] == 2:
    from ConfigParser import *
else:
    from configparser import *
