# type annotation
from __future__ import annotations  # 3.7
from typing import *

# mypy
s = None  # type: Optional[str]


# 3.5
# function annotation
def add_numbers(a: int, b: int) -> int:
    return a + b


print(add_numbers(4, 6))
print(add_numbers('hoge', 'fuga'))
print(add_numbers.__annotations__)

# 3.6
# variable annotation
my_string: str = ''
my_list: List[Union[int, str]] = []
my_dict: Dict[str, int] = {}

my_list += 'hoge'
my_list.append(3)
print(my_list)

# create Types at runtime
Ref = NewType("ReferenceCounts", Dict[str, int])
my_ref: Ref = {'test': 1}
print(type(my_ref))

# 3.7
# postponed evaluation
# optional in 3.x: from __future__ import annotations
# default in 4.0
