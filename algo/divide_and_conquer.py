"""
Recursively sum a range of numbers
Divide and Conquer
"""


def recursive_sum(lo, hi):  # hi: inclusive
    if hi - lo < 100_000:  # base case threshold
        return sum(range(lo, hi + 1))
    else:
        mid = (hi + lo) // 2  # middle index for splitting
        left = recursive_sum(lo, mid)
        right = recursive_sum(mid + 1, hi)
        return left + right


if __name__ == '__main__':
    total = recursive_sum(0, 100_000_000)
    print('Total sum is', total)
