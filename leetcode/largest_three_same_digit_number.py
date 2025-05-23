def largest_good_integer(num: str) -> str:
    """https://leetcode.com/problems/largest-3-same-digit-number-in-string"""
    largest = -1

    for i in range(len(num) - 2):
        if num[i] == num[i + 1] == num[i + 2]:
            largest = max(largest, int(num[i : i + 3]))

    return (str(largest) * 3)[:3] if largest >= 0 else ""
