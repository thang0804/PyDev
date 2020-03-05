import sys

from typing import (
    TypeVar, Iterator, Iterable, NoReturn, overload, Container,
    Sequence, MutableSequence, Mapping, MutableMapping, Tuple, List, Any, Dict, Callable, Generic,
    Set, AbstractSet, FrozenSet, MutableSet, Sized, Reversible, SupportsInt, SupportsFloat, SupportsAbs,
    SupportsComplex, IO, BinaryIO, Union,
    ItemsView, KeysView, ValuesView, ByteString, Optional, AnyStr, Type, Text,
    Protocol,
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


if sys.version_info[0] == 2:
    from io import open as open
    from future_builtins import ascii as ascii
    from future_builtins import oct as oct
    from future_builtins import hex as hex

    from __builtin__ import unichr as chr
    from __builtin__ import isinstance as isinstance
    from __builtin__ import raw_input as input

    # at runtime thse are not from __builtin__, but I think the signature is
    # the same, so should be fine for static analysis
    from __builtin__ import next as next
    from __builtin__ import round as round
    from __builtin__ import super as super

    @overload
    def max(__arg1: _T, __arg2: _T, *_args: _T, key: Callable[[_T], Any] = ...) -> _T: ...
    @overload
    def max(__iterable: Iterable[_T], *, key: Callable[[_T], Any] = ...) -> _T: ...
    @overload
    def max(__iterable: Iterable[_T], *, key: Callable[[_T], Any] = ..., default: _VT) -> Union[_T, _VT]: ...

    @overload
    def min(__arg1: _T, __arg2: _T, *_args: _T, key: Callable[[_T], Any] = ...) -> _T: ...
    @overload
    def min(__iterable: Iterable[_T], *, key: Callable[[_T], Any] = ...) -> _T: ...
    @overload
    def min(__iterable: Iterable[_T], *, key: Callable[[_T], Any] = ..., default: _VT) -> Union[_T, _VT]: ...

    @overload
    def pow(__x: int, __y: int) -> Any: ...  # The return type can be int or float, depending on y
    @overload
    def pow(__x: int, __y: int, __z: int) -> Any: ...
    @overload
    def pow(__x: float, __y: float) -> float: ...
    @overload
    def pow(__x: float, __y: float, __z: float) -> float: ...


    __all__ = ['ascii', 'chr', 'hex', 'input', 'isinstance', 'next', 'oct',
               'open', 'pow', 'round', 'super', 'max', 'min']

else:
    import builtins
    ascii = builtins.ascii
    chr = builtins.chr
    hex = builtins.hex
    input = builtins.input
    next = builtins.next
    # Only for backward compatibility with future v0.8.2:
    isinstance = builtins.isinstance
    oct = builtins.oct
    open = builtins.open
    pow = builtins.pow
    round = builtins.round
    super = builtins.super
    if sys.version_info[0:2] >= (3, 4):
        max = builtins.max
        min = builtins.min
        __all__ = []   # type: List[str]
    else:
        from future.builtins import newmax as max
        from future.builtins import newmin as min
        __all__ = ['min', 'max']
