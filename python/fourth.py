
from typing import List


def find_consecutive(numbers: List[int]) -> int:
    numbers.sort()

    expected_next = 1
    for num in numbers:
        if expected_next == num:
            expected_next += 1
    
    return expected_next


if __name__ == "__main__":
    assert find_consecutive([3, 4, -1, 1]) == 2
    assert find_consecutive([1, 2, 0]) == 3