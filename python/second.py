# Good morning! Here's your coding interview problem for today.
#
# This problem was asked by Uber.
#
# Given an array of integers, return a new array such that each element at index i of the new array is the product of
# all the numbers in the original array except the one at i.
#
# For example, if our input was [1, 2, 3, 4, 5], the expected output would be [120, 60, 40, 30, 24]. If our input was
# [3, 2, 1], the expected output would be [2, 3, 6].
#
# Follow-up: what if you can't use division?

from typing import List


def calculate(numbers: List) -> List:
    product = 1
    for num in numbers:
        product = num * product

    for i in range(len(numbers)):
        numbers[i] = product / numbers[i]

    return numbers


def calculate_no_division(numbers: List) -> List:
    new_array = []
    before = 1
    for i, num in enumerate(numbers):
        new_array.append(before)
        before = num * before

    after = 1
    for i, num in reversed(list(enumerate(numbers))):
        new_array[i] = after * new_array[i]
        after = after * num
    
    return new_array


if __name__ == "__main__":
    assert calculate([1, 2, 3, 4, 5]) == [120, 60, 40, 30, 24]
    assert calculate([3, 2, 1]) == [2, 3, 6]
    assert calculate_no_division([1, 2, 3, 4, 5]) == [120, 60, 40, 30, 24]
    assert calculate_no_division([3, 2, 1]) == [2, 3, 6]
