from itertools import product


def solution(n):
    """

    Args:
        n (int): 괄호쌍의 갯수
    Returns:
        int: 만들 수 있는 올바른 괄호 쌍의 갯수
    """
    dp = [set(), set(["()"])]  # index 사용 편의성을 위해 index = 0도 추가

    if n < 2:
        return len(dp[n])

    while len(dp) < n + 1:
        complete_parenthesis = set()
        for prev_result in dp[len(dp) - 1]:
            complete_parenthesis.add(f"({prev_result})")

        for i in range(1, len(dp)):
            left = dp[i]
            right = dp[len(dp) - i]

            for candidate in product(left, right):
                complete_parenthesis.add("".join(candidate))

        dp.append(complete_parenthesis)

    return len(dp[n])
