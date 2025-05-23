def duplicate(num: str) -> str:
    return num * 9  # nums[i] <= 10^9


def largest_numer(nums):
    nums = [str(num) for num in nums]
    duplicated_nums = list(map(duplicate, nums))

    numbers = [
        (duplicated, num) for duplicated, num in zip(duplicated_nums, nums)
    ]
    numbers.sort(reverse=True)  # duplicated 값을 사용해 정렬

    answer = "".join([num for _, num in numbers])
    if int(answer) == 0:
        answer = "0"

    return answer
