def remove_duplicates(nums):
    """
    https://leetcode.com/problems/remove-duplicates-from-sorted-array/description/?source=submission-ac

    Args:
        nums (List[int])
    Returns:
        int
    """
    duplicates_removed = list(set(nums))
    unique_count = len(duplicates_removed)

    duplicates_removed.sort()
    for i, value in enumerate(duplicates_removed):
        nums[i] = value

    return unique_count
