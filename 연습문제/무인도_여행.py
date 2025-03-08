DIRS = [
    [0, -1],
    [0, 1],
    [-1, 0],
    [1, 0],
]


def dfs(start, grid, visited):
    stack = list([start])
    days = 0

    while stack:
        i, j = stack.pop()

        if (i, j) in visited:
            continue
        if grid[i][j] == "X":
            continue

        visited.add((i, j))
        days += int(grid[i][j])

        for dir_ in DIRS:
            di, dj = dir_

            if not 0 <= i + di < len(grid):
                continue
            if not 0 <= j + dj < len(grid[i]):
                continue

            stack.append((i + di, j + dj))

    return days


def solution(maps):
    grid = [list(line) for line in maps]
    answer = list()

    visited = set()
    for i, _ in enumerate(maps):
        for j, _ in enumerate(maps[i]):
            start = (i, j)
            days = dfs(start, grid, visited)
            if days:
                answer.append(days)

    answer.sort()
    return answer if answer else [-1]
