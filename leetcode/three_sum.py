def three_sum(nums):
    """
    Args:
        nums: List[int]
    Returns:
        List[List[int]]
    """

    # 2. Fix a number: nums[i]
    #   - Then, find two numebers satisfies sum of both numbers to be -nums[i]
    nums.sort()
    triplets = set()
    length = len(nums)
    for i in range(length - 2):
        left = i + 1
        right = length - 1

        while left < right:
            sum_ = nums[i] + nums[left] + nums[right]
            if sum_ == 0:
                triplets.add((nums[i], nums[left], nums[right]))
                left += 1
                right -= 1
            elif sum_ < 0:
                left += 1
            else:
                right -= 1

    answer = [list(entity) for entity in triplets]
    answer.sort(key=lambda x: (x[0], x[1], x[2]))

    return answer
