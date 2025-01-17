def solution(sequence):
    partial_sum = [[0] * len(sequence) for _ in range(len(sequence))]

    pulse = [1, -1] * (len(sequence) // 2) + [1]
    sequence = [a * b for a, b in zip(sequence, pulse)]

    partial_sum[0][0] = sequence[0]
    start_index = 0
    for end_index, number in enumerate(sequence[1:], start=1):
        noted = partial_sum[start_index][end_index - 1]
        partial_sum[start_index][end_index] = noted + number

    for start_index, number_1 in enumerate(sequence[1:], start=1):
        for end_index, number_2 in enumerate(sequence[1:], start=1):
            partial_sum[start_index][end_index] = (
                partial_sum[start_index - 1][end_index]
                - sequence[start_index - 1]
            )

    return max(abs(num) for row in partial_sum for num in row)
