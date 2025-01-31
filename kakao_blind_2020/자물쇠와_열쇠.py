from copy import deepcopy


def place_key(key, total_map, m, i, j):
    for ki in range(m):
        for kj in range(m):
            total_map[i + ki][j + kj] += key[ki][kj]
    return total_map


def is_opened(total_map, n, m):
    for i in range(n):
        for j in range(n):
            if total_map[m - 1 + i][m - 1 + j] != 1:
                return False
    return True


def solution(key, lock):
    m = len(key)
    n = len(lock)

    # 1. key와 lock을 모두 놓을 수 있는 큰 판을 먼저 생성한다.
    total_map = [[0] * (n + 2 * m - 2) for _ in range(n + 2 * m - 2)]
    for i in range(n):
        for j in range(n):
            total_map[m - 1 + i][m - 1 + j] = lock[i][j]

    # 2. key를 0, 90, 180, 270도 회전한 경우를 모두 생성해둔다.
    key_1 = key  # 0 deg
    key_2 = list(zip(*key[::-1]))  # 90 deg
    key_3 = list(zip(*key_2[::-1]))  # 180 deg
    key_4 = list(zip(*key_3[::-1]))  # 270 deg
    keys = [key_1, key_2, key_3, key_4]

    # 3. key를 total_map의 모든 위치에 놓아보면서 lock을 열 수 있는지 확인한다.
    # - (m - 1, m - 1) ~ (m - 1 + n - 1, m - 1 + n - 1)까지 모두 1인 경우에 해당한다.
    for key in keys:
        for i in range(n + m - 1):
            for j in range(n + m - 1):
                updated_map = place_key(key, deepcopy(total_map), m, i, j)
                if is_opened(updated_map, n, m):
                    return True

    return False
