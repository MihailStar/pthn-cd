from __future__ import annotations

from dataclasses import dataclass
from enum import Enum
from typing import (
    Callable,
    Dict,
    Final,
    Iterable,
    List,
    Literal,
    Mapping,
    NamedTuple,
    Sequence,
    Set,
    Tuple,
    TypeAlias,
    TypedDict,
    TypeVar,
    Union,
)

lst_old: List[int] = [True, 2]
lst: list[int] = [True, 2]

tpl_old: Tuple[int, float] = (1, 2)
tpl: tuple[int, float] = (1, 2)

ints: tuple[int, ...] = ()

dct_old: Dict[int, float] = {True: 2}
dct: dict[int, float] = {True: 2}

st_old: Set[int] = {True, 2}
st: set[int] = {True, 2}

NnOld: TypeAlias = Union[int, float]
type Nn = int | float

FNL: Final[Literal[1]] = 1


class CrdntsViaNamedTuple(NamedTuple):
    latitude: float
    longitude: float

crdnts_nt = CrdntsViaNamedTuple(latitude=10, longitude=20)
crdnts_nt.latitude
crdnts_nt.longitude


CrdntsViaDictWithLiteral = dict[Literal["latitude"] | Literal["longitude"], float]

crdnts_dl: CrdntsViaDictWithLiteral = {"latitude": 10, "longitude": 20}
crdnts_dl["latitude"]
crdnts_dl["longitude"]


class CrdntsViaTypedDict(TypedDict):
    latitude: float
    longitude: float

crdnts_td = CrdntsViaTypedDict(latitude=10, longitude=20)
crdnts_td["latitude"]
crdnts_td["longitude"]


@dataclass
class CrdntsViaDataClass:
    latitude: float
    longitude: float

crdnts_dc = CrdntsViaDataClass(latitude=10, longitude=20)
crdnts_dc.latitude
crdnts_dc.longitude


class Status(Enum):
    SUCCESS = "success"
    ERROR = "error"
    Success = "success"
    Error = "error"


T = TypeVar("T")

def get_first_old(iterable: Iterable[T]) -> T | None:
    for item in iterable:
        return item

def get_first[T](iterable: Iterable[T]) -> T | None:
    for item in iterable:
        return item


def do_something_with_sequence[T](sequence: Sequence[T]) -> T | None:
    pass

def do_something_with_associative[T](associative: Mapping[str, T]) -> T | None:
    pass


type FuncA = Callable[[int, float], int]
type FuncB = Callable[..., int]


class Pnt:
    def __init__(self) -> None:
        pass

    def get_self_old(self) -> "Pnt":
        return self

    def get_self(self) -> Pnt:
        return self

p1 = Pnt()
p1.get_self_old()
p1.get_self()


def main() -> None:
    pass

main.__annotations__

if __name__ == "__main__":
    main()
