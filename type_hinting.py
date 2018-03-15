# type hinting


# 3.5
def add_numbers(a: int, b: int) -> int:
    return a + b


s = None  # type: Optional[str]
len(s)

# 3.6
my_string: str = ''
my_list: List[int] = []
my_dict: Dict[str, int] = {}
