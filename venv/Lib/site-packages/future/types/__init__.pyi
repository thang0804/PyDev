import sys

from typing import (
    TypeVar, Iterator, Iterable, overload, Container,
    Sequence, MutableSequence, Mapping, MutableMapping, NoReturn, Tuple, List, Any, Dict, Callable, Generic,
    Set, AbstractSet, FrozenSet, MutableSet, Sized, Reversible, SupportsInt, SupportsFloat,
    SupportsComplex, SupportsAbs, IO, Union, ItemsView, KeysView,
    ValuesView, ByteString, Optional, AnyStr, Type,
)

# Note that names imported above are not automatically made visible via the
# implicit builtins import.

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


newtypes: Dict[type, type]

if sys.version_info[0] >= 3:
    import builtins
    bytes = builtins.bytes
    dict = builtins.dict
    int = builtins.int
    list = builtins.list
    object = builtins.object
    range = builtins.range
    str = builtins.str

    __all__ = ['newtypes']

else:
    import __builtin__
    newbytes = __builtin__.bytes
    newint = __builtin__.int
    newlist = __builtin__.list
    newobject = __builtin__.object
    newstr = __builtin__.str

    class newrange(Sequence[int]):
        start: int
        stop: int
        step: int
        @overload
        def __init__(self, stop: int) -> None: ...
        @overload
        def __init__(self, start: int, stop: int, step: int = ...) -> None: ...
        def count(self, value: int) -> int: ...
        def index(self, value: int, start: int = ..., stop: Optional[int] = ...) -> int: ...
        def __len__(self) -> int: ...
        def __contains__(self, o: object) -> bool: ...
        def __iter__(self) -> Iterator[int]: ...
        @overload
        def __getitem__(self, i: int) -> int: ...
        @overload
        def __getitem__(self, s: slice) -> newrange: ...
        def __repr__(self) -> str: ...
        def __reversed__(self) -> Iterator[int]: ...

    class newdict(Dict[_KT, _VT]):
        def keys(self) -> KeysView[_KT]: ...  # type: ignore
        def values(self) -> ValuesView[_VT]: ...  # type: ignore
        def items(self) -> ItemsView[_KT, _VT]: ...  # type: ignore

    __all__ = ['newbytes', 'newdict', 'newint', 'newlist', 'newrange', 'newstr', 'newtypes']
