def solution(cookie):
    # DP문제: i번부터 j번 까지의 쿠키의 합 계산
    n = len(cookie)
    dp = [[0] * n for _ in range(n)]

    for index, cookies in enumerate(cookie):
        dp[index][index] = cookies

    for i in range(n):
        for j in range(i + 1, n):
            dp[i][j] += dp[i][j - 1] + cookie[j]

    maximum_cookies = 0
    for i in range(n - 1):
        for j in range(i, n - 1):
            left = dp[i][j]

            for k in range(j + 1, n):
                right = dp[j + 1][k]

                if left == right:
                    maximum_cookies = max(maximum_cookies, left)

    return maximum_cookies
