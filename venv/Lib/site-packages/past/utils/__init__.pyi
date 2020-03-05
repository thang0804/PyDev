
from typing import TypeVar, overload

_T = TypeVar('_T')

PY3: bool
PY2: bool
PYPY: bool


def with_metaclass(meta: type, *bases: type) -> type: ...

def native(obj: _T) -> _T: ...

# An alias for future.utils.old_div():
def old_div(a, b): ...

__all__ = ['PY3', 'PY2', 'PYPY', 'with_metaclass', 'native', 'old_div']
