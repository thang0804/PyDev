from __future__ import absolute_import
from typing import AnyStr, Text
import sys

if sys.version_info[0] >= 3:
    from urllib.request import *
    # This aren't in __all__:

    def proxy_bypass(host): ...
    def quote(s: AnyStr, safe: Text = ...) -> AnyStr: ...
    def unquote(s: AnyStr) -> AnyStr: ...

    # FIXME: create stubs for commented out functions:
    from urllib.request import (getproxies as getproxies,
                                pathname2url as pathname2url,
                                # request_host,
                                # thishost,
                                url2pathname as url2pathname,
                                urlcleanup as urlcleanup,
                                # urljoin,
                                urlopen as urlopen,
                                # urlparse,
                                urlretrieve as urlretrieve,
                                # urlsplit,
                                #urlunparse
                                )


    def splittype(url): ...
    def splithost(url): ...
    def splituser(host): ...
    def splitpasswd(user): ...
    def splitport(host): ...
    def splitnport(host, defport=...): ...
    def splitquery(url): ...
    def splittag(url): ...
    def splitattr(url): ...
    def splitvalue(attr): ...

else:
    __future_module__ = True
    # copied from third_party/2/six/moves/urllib/request
    from urllib2 import urlopen as urlopen
    from urllib2 import install_opener as install_opener
    from urllib2 import build_opener as build_opener
    from urllib import pathname2url as pathname2url
    from urllib import url2pathname as url2pathname
    from urllib import getproxies as getproxies
    from urllib2 import Request as Request
    from urllib2 import OpenerDirector as OpenerDirector
    from urllib2 import HTTPDefaultErrorHandler as HTTPDefaultErrorHandler
    from urllib2 import HTTPRedirectHandler as HTTPRedirectHandler
    from urllib2 import HTTPCookieProcessor as HTTPCookieProcessor
    from urllib2 import ProxyHandler as ProxyHandler
    from urllib2 import BaseHandler as BaseHandler
    from urllib2 import HTTPPasswordMgr as HTTPPasswordMgr
    from urllib2 import HTTPPasswordMgrWithDefaultRealm as HTTPPasswordMgrWithDefaultRealm
    from urllib2 import AbstractBasicAuthHandler as AbstractBasicAuthHandler
    from urllib2 import HTTPBasicAuthHandler as HTTPBasicAuthHandler
    from urllib2 import ProxyBasicAuthHandler as ProxyBasicAuthHandler
    from urllib2 import AbstractDigestAuthHandler as AbstractDigestAuthHandler
    from urllib2 import HTTPDigestAuthHandler as HTTPDigestAuthHandler
    from urllib2 import ProxyDigestAuthHandler as ProxyDigestAuthHandler
    from urllib2 import HTTPHandler as HTTPHandler
    from urllib2 import HTTPSHandler as HTTPSHandler
    from urllib2 import FileHandler as FileHandler
    from urllib2 import FTPHandler as FTPHandler
    from urllib2 import CacheFTPHandler as CacheFTPHandler
    from urllib2 import UnknownHandler as UnknownHandler
    from urllib2 import HTTPErrorProcessor as HTTPErrorProcessor
    from urllib import urlretrieve as urlretrieve
    from urllib import urlcleanup as urlcleanup
    from urllib import URLopener as URLopener
    from urllib import FancyURLopener as FancyURLopener
    from urllib import proxy_bypass as proxy_bypass
    from urllib2 import parse_http_list as parse_http_list
    from urllib2 import parse_keqv_list as parse_keqv_list

    from urlparse import *

    # Rename:
    from urllib import toBytes    # missing from __all__ on Py2.6
    to_bytes = toBytes

    # from urllib import (pathname2url,
    #                     url2pathname,
    #                     getproxies,
    #                     urlretrieve,
    #                     urlcleanup,
    #                     URLopener,
    #                     FancyURLopener,
    #                     proxy_bypass)

    # from urllib2 import (
    #                  AbstractBasicAuthHandler,
    #                  AbstractDigestAuthHandler,
    #                  BaseHandler,
    #                  CacheFTPHandler,
    #                  FileHandler,
    #                  FTPHandler,
    #                  HTTPBasicAuthHandler,
    #                  HTTPCookieProcessor,
    #                  HTTPDefaultErrorHandler,
    #                  HTTPDigestAuthHandler,
    #                  HTTPErrorProcessor,
    #                  HTTPHandler,
    #                  HTTPPasswordMgr,
    #                  HTTPPasswordMgrWithDefaultRealm,
    #                  HTTPRedirectHandler,
    #                  HTTPSHandler,
    #                  URLError,
    #                  build_opener,
    #                  install_opener,
    #                  OpenerDirector,
    #                  ProxyBasicAuthHandler,
    #                  ProxyDigestAuthHandler,
    #                  ProxyHandler,
    #                  Request,
    #                  UnknownHandler,
    #                  urlopen,
    #                 )

    # from urlparse import (
    #                  urldefrag
    #                  urljoin,
    #                  urlparse,
    #                  urlunparse,
    #                  urlsplit,
    #                  urlunsplit,
    #                  parse_qs,
    #                  parse_q"
    #                 )
