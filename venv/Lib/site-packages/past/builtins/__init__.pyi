import sys
from typing import (
    Any, AnyStr, Callable, Dict, Iterable, Mapping, NoReturn, List, Optional,
    Pattern, Text, Tuple, Type, TypeVar, Union, overload, ValuesView, KeysView, ItemsView,
)

_T = TypeVar('_T')
_T_co = TypeVar('_T_co', covariant=True)
_KT = TypeVar('_KT')
_VT = TypeVar('_VT')
_S = TypeVar('_S')
_T1 = TypeVar('_T1')
_T2 = TypeVar('_T2')
_T3 = TypeVar('_T3')
_T4 = TypeVar('_T4')
_T5 = TypeVar('_T5')
_TT = TypeVar('_TT', bound='type')

# from past.builtins.misc import (ascii, hex, input, oct, open)
if sys.version_info[0] >= 3:
    from past.types import basestring as basestring
    from past.types import olddict as dict
    from past.types import oldstr as str
    from past.types import long as long
    from past.types import unicode as unicode

    def apply(f: Callable[..., _T], *args: Any, **kw: Any) -> _T: ...
    def chr(i: int) -> bytes: ...
    def cmp(x: Any, y: Any) -> int: ...
    from sys import intern as intern
    def oct(number: int) -> unicode: ...
    from builtins import input as raw_input
    from imp import reload as reload
    from builtins import str as unicode
    from builtins import chr as unichr
    from builtins import range as xrange

    # copied from __builtins__.pyi
    @overload
    def filter(__function: Callable[[AnyStr], Any],  # type: ignore
               __iterable: AnyStr) -> AnyStr: ...
    @overload
    def filter(__function: None,  # type: ignore
               __iterable: Tuple[Optional[_T], ...]) -> Tuple[_T, ...]: ...
    @overload
    def filter(__function: Callable[[_T], Any],  # type: ignore
               __iterable: Tuple[_T, ...]) -> Tuple[_T, ...]: ...
    @overload
    def filter(__function: None,
               __iterable: Iterable[Optional[_T]]) -> List[_T]: ...
    @overload
    def filter(__function: Callable[[_T], Any],
               __iterable: Iterable[_T]) -> List[_T]: ...

    @overload
    def map(__func: None, __iter1: Iterable[_T1]) -> List[_T1]: ...
    @overload
    def map(__func: None,
            __iter1: Iterable[_T1],
            __iter2: Iterable[_T2]) -> List[Tuple[_T1, _T2]]: ...
    @overload
    def map(__func: None,
            __iter1: Iterable[_T1],
            __iter2: Iterable[_T2],
            __iter3: Iterable[_T3]) -> List[Tuple[_T1, _T2, _T3]]: ...
    @overload
    def map(__func: None,
            __iter1: Iterable[_T1],
            __iter2: Iterable[_T2],
            __iter3: Iterable[_T3],
            __iter4: Iterable[_T4]) -> List[Tuple[_T1, _T2, _T3, _T4]]: ...
    @overload
    def map(__func: None,
            __iter1: Iterable[_T1],
            __iter2: Iterable[_T2],
            __iter3: Iterable[_T3],
            __iter4: Iterable[_T4],
            __iter5: Iterable[_T5]) -> List[Tuple[_T1, _T2, _T3, _T4, _T5]]: ...
    @overload
    def map(__func: None,
            __iter1: Iterable[Any],
            __iter2: Iterable[Any],
            __iter3: Iterable[Any],
            __iter4: Iterable[Any],
            __iter5: Iterable[Any],
            __iter6: Iterable[Any],
            *iterables: Iterable[Any]) -> List[Tuple[Any, ...]]: ...
    @overload
    def map(__func: Callable[[_T1], _S], __iter1: Iterable[_T1]) -> List[_S]: ...
    @overload
    def map(__func: Callable[[_T1, _T2], _S],
            __iter1: Iterable[_T1],
            __iter2: Iterable[_T2]) -> List[_S]: ...
    @overload
    def map(__func: Callable[[_T1, _T2, _T3], _S],
            __iter1: Iterable[_T1],
            __iter2: Iterable[_T2],
            __iter3: Iterable[_T3]) -> List[_S]: ...
    @overload
    def map(__func: Callable[[_T1, _T2, _T3, _T4], _S],
            __iter1: Iterable[_T1],
            __iter2: Iterable[_T2],
            __iter3: Iterable[_T3],
            __iter4: Iterable[_T4]) -> List[_S]: ...
    @overload
    def map(__func: Callable[[_T1, _T2, _T3, _T4, _T5], _S],
            __iter1: Iterable[_T1],
            __iter2: Iterable[_T2],
            __iter3: Iterable[_T3],
            __iter4: Iterable[_T4],
            __iter5: Iterable[_T5]) -> List[_S]: ...
    @overload
    def map(__func: Callable[..., _S],
            __iter1: Iterable[Any],
            __iter2: Iterable[Any],
            __iter3: Iterable[Any],
            __iter4: Iterable[Any],
            __iter5: Iterable[Any],
            __iter6: Iterable[Any],
            *iterables: Iterable[Any]) -> List[_S]: ...

    def range(__x: int, __y: int = ..., __step: int = ...) -> List[int]: ...

    from functools import reduce as reduce

    @overload
    def zip(__iter1: Iterable[_T1]) -> List[Tuple[_T1]]: ...
    @overload
    def zip(__iter1: Iterable[_T1],
            __iter2: Iterable[_T2]) -> List[Tuple[_T1, _T2]]: ...
    @overload
    def zip(__iter1: Iterable[_T1], __iter2: Iterable[_T2],
            __iter3: Iterable[_T3]) -> List[Tuple[_T1, _T2, _T3]]: ...
    @overload
    def zip(__iter1: Iterable[_T1], __iter2: Iterable[_T2], __iter3: Iterable[_T3],
            __iter4: Iterable[_T4]) -> List[Tuple[_T1, _T2, _T3, _T4]]: ...
    @overload
    def zip(__iter1: Iterable[_T1], __iter2: Iterable[_T2], __iter3: Iterable[_T3],
            __iter4: Iterable[_T4], __iter5: Iterable[_T5]) -> List[Tuple[_T1, _T2, _T3, _T4, _T5]]: ...
    @overload
    def zip(__iter1: Iterable[Any], __iter2: Iterable[Any], __iter3: Iterable[Any],
            __iter4: Iterable[Any], __iter5: Iterable[Any], __iter6: Iterable[Any],
            *iterables: Iterable[Any]) -> List[Tuple[Any, ...]]: ...

else:
    from __builtin__ import basestring as basestring
    from __builtin__ import dict as dict
    from __builtin__ import str as str
    from __builtin__ import long as long
    from __builtin__ import unicode as unicode

    from __builtin__ import apply as apply
    from __builtin__ import chr as chr
    from __builtin__ import cmp as cmp
    from __builtin__ import execfile as execfile
    from __builtin__ import intern as intern
    from __builtin__ import oct as oct
    from __builtin__ import raw_input as raw_input
    from __builtin__ import reload as reload
    from __builtin__ import unichr as unichr
    from __builtin__ import xrange as xrange

    from __builtin__ import filter as filter
    from __builtin__ import map as map
    from __builtin__ import range as range
    from __builtin__ import reduce as reduce
    from __builtin__ import zip as zip


if sys.version_info[0] >= 3:
    # We only import names that shadow the builtins on Py3. No other namespace
    # pollution on Py3.

    # Only shadow builtins on Py3; no new names
    __all__ = ['filter', 'map', 'range', 'reduce', 'zip',
               'basestring', 'dict', 'str', 'long', 'unicode',
               'apply', 'chr', 'cmp', 'execfile', 'intern', 'raw_input',
               'reload', 'unichr', 'xrange'
              ]

else:
    # No namespace pollution on Py2
    __all__ = []  # type: List[str]
