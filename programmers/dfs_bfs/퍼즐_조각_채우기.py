from typing import List
from pprint import pprint


DIRS = [
    [0, -1],
    [0, 1],
    [-1, 0],
    [1, 0],
]


def find_areas(grid: List[List[int]], target: int):
    """
    Returns:
        List[List[List[int]]]: 주어진 grid에서 target 값을 가진 블록들의 좌표들을 반환한다.
                        하나의 도형은 하나의 List[List[int]] 이다.
    """
    visited = [[False] * len(grid[0]) for _ in range(len(grid))]
    areas = list()

    def dfs(x, y, area):
        if visited[x][y]:
            return

        visited[x][y] = True
        area.append([x, y])

        for dx, dy in DIRS:
            nx, ny = x + dx, y + dy
            if (
                0 <= nx < len(grid)
                and 0 <= ny < len(grid[0])
                and not visited[nx][ny]
                and grid[nx][ny] == target
            ):
                dfs(nx, ny, area)

    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if not visited[i][j] and grid[i][j] == target:
                area = []
                dfs(i, j, area)
                areas.append(area)

    return areas


def normalize(block: List[List[int]]):
    """
    Returns:
        Tuple[Tuple[int, int]]:
            가장 x와 y값이 작은 블록의 좌표를 (0, 0)으로 삼고
            나머지 좌표들을 상대적으로 변환한 블록의 좌표를 반환한다.
            단, 원점으로부터의 거리가 같은 1칸 블록이 2개 이상일 경우 x값이 작은 것을 기준으로 한다.
    """
    min_x = min(block, key=lambda x: x[0])[0]
    min_y = min(block, key=lambda x: x[1])[1]

    return tuple(sorted((x - min_x, y - min_y) for x, y in block))


def rotate_block(block: List[List[int]]):
    """
    Returns:
        Tuple[Tuple[int, int]]: 90-degree rotated block (ccw)
    """
    return tuple((-y, x) for x, y in block)


def is_fit(area: List[List[int]], candidates):
    """
    Returns:
        bool: area의 모양이 candidates에 포함되는지를 찾는다.
    """
    area_set = set(tuple(point) for point in area)

    for candidate in candidates:
        if len(area) != len(candidate):
            continue

        if area_set == set(candidate):
            return True

    return False


def solution(game_board, table):
    # 1. board에서 빈 칸 찾기
    # - 빈 칸 좌표들을 찾은 후, x와 y가 가장 작은 값을 기준으로 normalize 한다.((0,0)으로 설정)
    # 2. table에서 도형 형태 찾기
    # - 마찬가지로 각 도형들을 찾은 후 x와 y가 가장 작은 값을 기준으로 normalize 한다.
    # - 이 도형들을 다시 90, 180, 270도 회전시킨 후 또 normalize 한다.
    # 3. 1에서 찾은 결과가 2에서 만든 결과에 속해있으면 해당 블록을 놓을 수 있다(count 증가)
    # 4. 최종 count를 반환한다.
    empty_areas = find_areas(game_board, 0)
    blocks = find_areas(table, 1)

    candidates = set()
    for block in blocks:
        quater_rotated_block = rotate_block(block)
        half_rotated_block = rotate_block(quater_rotated_block)
        three_quater_rotated_block = rotate_block(half_rotated_block)

        candidates.update(
            {
                normalize(block),
                normalize(quater_rotated_block),
                normalize(half_rotated_block),
                normalize(three_quater_rotated_block),
            }
        )

    filled_areas = [False] * len(empty_areas)

    count = 0
    for i, area in enumerate(empty_areas):
        if filled_areas[i]:
            continue

        normalized_area = normalize(area)
        if is_fit(normalized_area, candidates):
            filled_areas[i] = True
            count += len(normalized_area)
            break

    return count
