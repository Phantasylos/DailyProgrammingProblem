# Good morning! Here's your coding interview problem for today.
#
# This problem was asked by Stripe.
#
# Given an array of integers, find the first missing positive integer in linear time and constant space. In other
# words, find the lowest positive integer that does not exist in the array. The array can contain duplicates and
# negative numbers as well.
#
# For example, the input [3, 4, -1, 1] should give 2. The input [1, 2, 0] should give 3.
#
# You can modify the input array in-place.

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