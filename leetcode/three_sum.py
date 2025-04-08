def three_sum(nums):
    """
    Args:
        nums: List[int]
    Returns:
        List[List[int]]
    """

    # 1. Naive solution: O(N^3)
    #   - Expect: Timed Out
    nums.sort()
    triplets = set()
    length = len(nums)
    for i in range(length - 2):
        for j in range(i + 1, length - 1):
            for k in range(j + 1, length):
                a = nums[i]
                b = nums[j]
                c = nums[k]
                if a + b + c == 0:
                    triplets.add((a, b, c))

    answer = [list(entity) for entity in triplets]
    answer.sort(key=lambda x: (x[0], x[1], x[2]))

    return answer
