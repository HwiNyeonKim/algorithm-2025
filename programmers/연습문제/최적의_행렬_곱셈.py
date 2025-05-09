def solution(matrix_sizes):
    # i-j 까지의 행렬곱셈을 수행했을 때의 곱셈 연산 횟수
    dp = [[0] * len(matrix_sizes) for _ in range(len(matrix_sizes))]

    for matrix_count in range(1, len(matrix_sizes)):
        for i in range(len(matrix_sizes) - matrix_count):
            j = i + matrix_count
            dp[i][j] = float("inf")  # type: ignore
            for k in range(i, j):  # middle
                row = matrix_sizes[i][0]
                middle = matrix_sizes[k][1]
                column = matrix_sizes[j][1]

                dp[i][j] = min(
                    dp[i][j], dp[i][k] + row * middle * column + dp[k + 1][j]
                )

    return dp[0][-1]
