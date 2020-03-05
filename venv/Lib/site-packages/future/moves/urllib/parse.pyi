from __future__ import absolute_import

import sys

if sys.version_info[0] >= 3:
    from urllib.parse import *
else:
    __future_module__ = True
    from urlparse import (ParseResult, SplitResult, parse_qs, parse_qsl,
                          urldefrag, urljoin, urlparse, urlsplit,
                          urlunparse, urlunsplit)

    from urllib import (quote,
                        quote_plus,
                        unquote,
                        unquote_plus,
                        urlencode,
                        splitquery)
