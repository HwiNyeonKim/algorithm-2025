def sort_colors(nums):
    """https://leetcode.com/problems/sort-colors/description/

    Args:
        nums (List[int])
    """
    counter = {0: 0, 1: 0, 2: 0}

    for num in nums:
        counter[num] += 1

    current_index = 0
    for color, repeat in counter.items():
        for i in range(current_index, current_index + repeat):
            nums[i] = color

        current_index += repeat
