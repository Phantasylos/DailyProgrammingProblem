from typing import List


def caluclate(numbers: List) -> List:
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
    assert caluclate([1, 2, 3, 4, 5]) == [120, 60, 40, 30, 24]
    assert caluclate([3, 2, 1]) == [2, 3, 6]
    assert calculate_no_division([1, 2, 3, 4, 5]) == [120, 60, 40, 30, 24]
    assert calculate_no_division([3, 2, 1]) == [2, 3, 6]
