def remove_duplicates(nums):
    """
    https://leetcode.com/problems/remove-duplicates-from-sorted-array/description/?source=submission-ac

    Args:
        nums (List[int])
    Returns:
        int
    """
    prev = float("-inf")
    ptr = 0  # index
    current_index = 0

    while current_index < len(nums):
        current_value = nums[current_index]
        if current_value != prev:
            nums[ptr] = current_value
            prev = current_value
            ptr += 1

        current_index += 1

    return ptr
