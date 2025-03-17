from collections import deque

DIRS = [
    [-1, 0],
    [1, 0],
    [0, -1],
    [0, 1],
]


def move(grid, from_, dir_):
    # 가장자리 또는 벽에 다다를 때 까지 이동
    i, j = from_
    di, dj = dir_

    while (
        0 <= i + di < len(grid)
        and 0 <= j + dj < len(grid[i + di])
        and grid[i + di][j + dj] != "D"
    ):
        i += di
        j += dj

    return i, j


def solution(board):
    # Setup
    grid = [list(row) for row in board]
    for i, row in enumerate(grid):
        for j, value in enumerate(row):
            if value == "R":
                start = (i, j)
            elif value == "G":
                goal = (i, j)

    # Solve
    queue = deque([(start, 0)])
    visited = set([start])
    while queue:
        (from_), steps = queue.popleft()

        for dir_ in DIRS:
            to = move(grid, from_, dir_)

            if to in visited:
                continue

            if to == goal:
                return steps + 1

            visited.add(to)
            queue.append((to, steps + 1))

    return -1
