# 물건의 갯수는 최대 40개이고, 한번에 남기는 흔적은 최대 3개이므로 적당히 121 이상의 값을 천장으로 쓴다
INF = 999


def solution(info, n, m):
    # 전형적인 knapsack 문제와 같은 형태이다.
    # - 여기서는 **A의 흔적을 최소화**하면서, **B의 흔적을 최대화**하는 형태로 변형되었다.

    # DP table: i번째(row) 불건까지 훔치고 B가 남긴 흔적이 b개(col)일 때, A가 남긴 흔적
    dp = [[INF] * (m) for _ in range(len(info) + 1)]

    # 초기 상태 설정: 물건을 하나도 훔치지 않은 상태
    dp[0][0] = 0

    for i in range(len(info)):
        # i 번쨰 물건을 훔치려고 한다.
        trace_a, trace_b = info[i]

        # i - 1개의 물건을 훔쳤을 때, B가 남긴 흔적의 갯수
        for b in range(m):
            if dp[i][b] == INF:
                # B가 b만큼의 흔적을 남기고 i 번째 물건을 훔칠 수 없는 경우
                continue

            # A가 i번째 물건을 훔치는게 더 나은 경우를 찾아 업데이트
            # * A의 제한 흔적 초과는 여기서는 고려하지 않는다. 마지막에 한 번만 확인한다.
            dp[i + 1][b] = min(dp[i + 1][b], dp[i][b] + trace_a)

            # B가 i번째 물건을 훔치는게 더 나은 경우를 찾아 업데이트
            next_b = b + trace_b
            if next_b < m:
                dp[i + 1][next_b] = min(dp[i + 1][next_b], dp[i][b])

    # 물건을 모두 훔치는 경우 중 A의 흔적이 최소가 되는 경우를 찾는다.
    minimum_trace_a = min(dp[-1])

    return minimum_trace_a if minimum_trace_a < n else -1
