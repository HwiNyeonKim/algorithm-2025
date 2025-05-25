from itertools import combinations, product


def is_done(current, target):
    for current_line, target_line in zip(current, target):
        for c, t in zip(current_line, target_line):
            if c != t:
                return False
    return True


def flip_row(current, index):
    current[index] = [1 if c == 0 else 0 for c in current[index]]


def flip_column(current, index):
    for row in current:
        row[index] = 1 if row[index] == 0 else 0


def solution(beginning, target):
    n = len(target)
    m = len(target[0])
    minimum_count = float("inf")

    # flip_row를 0~n번 수행 x flip_column을 0~m번 수행
    row_indices = [i for i in range(n)]
    column_indices = [i for i in range(m)]

    row_cases = [
        combination
        for i in range(n + 1)
        for combination in combinations(row_indices, i)
    ]
    column_cases = [
        combination
        for i in range(m + 1)
        for combination in combinations(column_indices, i)
    ]

    for rows, columns in product(row_cases, column_cases):
        board = [row[:] for row in beginning]

        for row in rows:
            flip_row(board, row)
        for column in columns:
            flip_column(board, column)

        if is_done(board, target):
            minimum_count = min(minimum_count, len(rows) + len(columns))

    return -1 if minimum_count == float("inf") else minimum_count
