from itertools import combinations


def subsets(nums):
    """
    https://leetcode.com/problems/subsets/description/

    Args:
        nums (List[int])
    Returns:
        List[List[int]]
    """
    subsets = list()

    for i in range(len(nums) + 1):
        for pick in combinations(nums, i):
            subsets.append(list(pick))

    return subsets
