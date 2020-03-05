from __future__ import absolute_import
import sys

if sys.version_info[0] >= 3:
    from xmlrpc.server import *
else:
    from xmlrpclib import *
