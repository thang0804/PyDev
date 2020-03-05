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


if sys.version_info[0] == 2:
    import __builtin__
    basestring = __builtin__.basestring
    dict = __builtin__.dict
    str = __builtin__.str
    long = __builtin__.long
    unicode = __builtin__.unicode
    __all__ = []  # type: List[str]
else:
    basestring = (bytes, str)
    oldstr = bytes
    long = int
    unicode = str

    class olddict(Dict[_KT, _VT]):

        # change return type
        def keys(self) -> List[_KT]: ...  # type: ignore
        def values(self) -> List[_VT]: ...  # type: ignore
        def items(self) -> List[Tuple[_KT, _VT]]: ...  # type: ignore

        # backport
        def iterkeys(self) -> Iterator[_KT]: ...
        def itervalues(self) -> Iterator[_VT]: ...
        def iteritems(self) -> Iterator[Tuple[_KT, _VT]]: ...
        def viewkeys(self) -> KeysView[_KT]: ...
        def viewvalues(self) -> ValuesView[_VT]: ...
        def viewitems(self) -> ItemsView[_KT, _VT]: ...
        def has_key(self, k: _KT) -> bool: ...

    __all__ = ['basestring', 'olddict', 'oldstr', 'long', 'unicode']
