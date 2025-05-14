def solution(cookie):
    n = len(cookie)
    prefix_sum = [0] * (n + 1)

    for i in range(n):
        prefix_sum[i + 1] = prefix_sum[i] + cookie[i]  # prefix_sum[0] = 0

    max_cookie = 0
    for m in range(n - 1):
        l = m  # noqa
        r = m + 1

        while 0 <= l and r < n:
            left = prefix_sum[m + 1] - prefix_sum[l]  # [l + 1, m]
            right = prefix_sum[r + 1] - prefix_sum[m + 1]  # [m + 1, r]

            if left == right:
                max_cookie = max(max_cookie, left)
                l -= 1
                r += 1
            elif left < right:
                l -= 1
            else:
                r += 1

    return max_cookie
