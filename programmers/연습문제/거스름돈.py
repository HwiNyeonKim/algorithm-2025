def solution(n, money):
    """
    Args:
        n (int): 거슬러 줘야 하는 돈, [1, 100_000]
        money (List[int]): 화폐 단위, 최대 100종류
    Returns:
        int: 거슬러줄 수 있는 방법의 가짓수를 1_000_000_007로 나눈 나머지
    """
    # Default Setup
    dp = [0] * (n + 1)
    dp[0] = 1

    # Calc
    for coin in money:
        for change in range(coin, n + 1):
            dp[change] += dp[change - coin]

    return dp[n] % 1_000_000_007
