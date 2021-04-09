from dataclasses import dataclass, field, InitVar, asdict, astuple
import typing
import uuid


@dataclass(
    init=True,
    repr=True,
    eq=True,
    order=False,
    unsafe_hash=False,
    frozen=False,
)  # all defaults
class Customer:
    id: int
    name: str


@dataclass(unsafe_hash=True)  # mutable, hashable
class Customer1:
    id: int
    name: str = "Nanashi"  # default value


@dataclass
class Customer2:
    _grade: InitVar[typing.Any]  # Init-only variable
    id: int
    name: str

    def __post_init__(self, _grade):
        self.name = self.name.upper()
        self.grade = str(_grade)


@dataclass(frozen=True, order=True)  # immutable, hashable, sortable
class CustomerOrder:
    processing_time: typing.ClassVar[int] = 999  # class variable
    id: uuid.UUID = field(
        compare=False, default_factory=uuid.uuid4, init=False)
    value: float = field(compare=True)
    product: str = field(compare=False)


@dataclass(frozen=True)  # frozenはsuperクラスと一致させる必要がある
class CustomerOrderExtended(CustomerOrder):
    date_ordered: str


if __name__ == '__main__':
    c = Customer1(1, "hogehoge")
    print(repr(c))
    print(hash(c))
    c.id = 2
    print(hash(c))

    c2 = Customer2("High", 1, "hogehoge")
    print(c2)
    # print(c2._grade)  # NG
    print(c2.grade)

    orders = [CustomerOrder(10.0, "Order1"),
              CustomerOrder(5.0, "Order2"),
              CustomerOrder(9.9, "Order3")]
    print(sorted(orders))

    co = CustomerOrderExtended(20.0, "Hoge", "2020/01/23")
    print(asdict(co))
    print(astuple(co))

    print(CustomerOrderExtended(5.0, "Order1", "2019/01/23")
          > CustomerOrderExtended(5.0, "Order2", "2020/01/23"))
