import pytest
from dfs_bfs import solution_bfs, solution_dfs


def generate_complex_case_1():
    """트리 + 사이클 구조"""
    n = 1000
    computers = [[0] * n for _ in range(n)]

    # 트리 구조 생성
    for i in range(1, 500):
        computers[i][(i - 1) // 2] = 1
        computers[(i - 1) // 2][i] = 1

    # 사이클 생성
    for i in range(500, 1000):
        computers[i][(i + 1) % 500 + 500] = 1
        computers[(i + 1) % 500 + 500][i] = 1

    # 트리와 사이클 연결
    computers[0][500] = 1
    computers[500][0] = 1

    return computers


def generate_complex_case_2():
    """트리 + 사이클 구조 (10000 노드)"""
    n = 10000
    computers = [[0] * n for _ in range(n)]

    # 트리 구조 생성
    for i in range(1, 5000):
        computers[i][(i - 1) // 2] = 1
        computers[(i - 1) // 2][i] = 1

    # 사이클 생성
    for i in range(5000, 10000):
        computers[i][(i + 1) % 5000 + 5000] = 1
        computers[(i + 1) % 5000 + 5000][i] = 1

    # 트리와 사이클 연결
    computers[0][5000] = 1
    computers[5000][0] = 1

    return computers


def generate_complex_case_3():
    """스타 그래프"""
    n = 1000
    computers = [[0] * n for _ in range(n)]

    # 중앙 노드(0)에 모든 노드 연결
    for i in range(1, n):
        computers[0][i] = computers[i][0] = 1

    return computers


def generate_complex_case_4():
    """스타 그래프 (10000 노드)"""
    n = 10000
    computers = [[0] * n for _ in range(n)]

    # 중앙 노드(0)에 모든 노드 연결
    for i in range(1, n):
        computers[0][i] = computers[i][0] = 1

    return computers


@pytest.mark.parametrize(
    "n, computers, expected",
    [
        [3, [[1, 1, 0], [1, 1, 0], [0, 0, 1]], 2],
        [3, [[1, 1, 0], [1, 1, 1], [0, 1, 1]], 1],
        [1000, generate_complex_case_1(), 1],
        # [10000, generate_complex_case_2(), 1],
        [1000, generate_complex_case_3(), 1],
        # [10000, generate_complex_case_4(), 1]
    ],
)
def test_네트워크_bfs(n, computers, expected):
    answer = solution_bfs(n, computers)

    assert answer == expected


@pytest.mark.parametrize(
    "n, computers, expected",
    [
        [3, [[1, 1, 0], [1, 1, 0], [0, 0, 1]], 2],
        [3, [[1, 1, 0], [1, 1, 1], [0, 1, 1]], 1],
        [1000, generate_complex_case_1(), 1],
        # [10000, generate_complex_case_2(), 1],
        [1000, generate_complex_case_3(), 1],
        # [10000, generate_complex_case_4(), 1]
    ],
)
def test_네트워크_dfs(n, computers, expected):
    answer = solution_dfs(n, computers)

    assert answer == expected
