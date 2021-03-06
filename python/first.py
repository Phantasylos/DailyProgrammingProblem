# Good morning! Here's your coding interview problem for today.
#
# This problem was recently asked by Google.
#
# Given a list of numbers and a number k, return whether any two numbers from the list add up to k.
#
# For example, given [10, 15, 3, 7] and k of 17, return true since 10 + 7 is 17.
#
# Bonus: Can you do this in one pass?


from typing import List


def solve(nums: List, target: int) -> bool:
    for i in range(len(nums)):
        if target - nums[i] in nums[i+1]:
            return True

    return False


if __name__ == "__main__":
    assert(solve([10, 15, 3, 7], 17) == True)