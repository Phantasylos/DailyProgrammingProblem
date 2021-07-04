from typing import List


def solve(nums: List, target: int) -> bool:
    for i in range(len(nums)):
        if target - nums[i] in nums[i+1]:
            return True

    return False


if __name__ == "__main__":
    assert(solve([10, 15, 3, 7], 17) == True)