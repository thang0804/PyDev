from __future__ import absolute_import
import sys

from subprocess import *

if sys.version_info[0] == 2:
    __future_module__ = True
    from commands import getoutput, getstatusoutput

if sys.version_info[0:2] == (2, 6):
    from future.backports.misc import check_output
