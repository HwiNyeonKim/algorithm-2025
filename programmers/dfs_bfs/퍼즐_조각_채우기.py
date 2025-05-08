DIRS = [
    [0, -1],
    [0, 1],
    [-1, 0],
    [1, 0],
]


def find_areas(grid, target):
    """
    Args:
        grid (List[List[int]]): 2차원 배열
        target (int): 찾고자 하는 값

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


def shift_to_origin(block):
    """
    Args:
        block (List[List[int]]): 블록의 좌표 리스트

    Returns:
        List[List[int, int]]: 원점에서 가장 가까운 좌표를 원점으로 이동시킨 블록의 좌표 리스트
                            x 좌표를먼저 비교하고, 그 다음 y좌표를 비교한다.
    """
    origin = min(block, key=lambda point: (point[0], point[1]))
    shifted = [(x - origin[0], y - origin[1]) for x, y in block]
    shifted.sort()

    return shifted


def get_rotated_blocks(block):
    """
    Args:
        block (List[List[int]]): 블록의 좌표 리스트

    Returns:
        List[List[List[int, int]]]: 90, 180, 270-deg 만큼 ccw 회전한 블록들의 좌표 리스트
    """

    def _rotate(block):
        return [(-y, x) for x, y in block]

    rotated_blocks = [block]
    for _ in range(3):
        rotated_blocks.append(_rotate(rotated_blocks[-1]))

    return rotated_blocks


def solution(game_board, table):
    empty_areas = find_areas(game_board, 0)
    shifted_empty_areas = [shift_to_origin(area) for area in empty_areas]

    blocks = find_areas(table, 1)
    all_block_shapes = list()
    for block in blocks:
        all_block_shapes.append(
            [shift_to_origin(rotated) for rotated in get_rotated_blocks(block)]
        )

    # 가장 많은 영역을 채우려면, 주어진 문제 조건 하에서 가장 큰 영역부터 채워야 한다.
    shifted_empty_areas.sort(key=lambda x: len(x), reverse=True)

    count = 0
    block_used = [False] * len(all_block_shapes)
    for area in shifted_empty_areas:
        for i, block_shapes in enumerate(all_block_shapes):
            if block_used[i]:
                continue

            if area in block_shapes:
                block_used[i] = True
                count += len(area)
                break

    return count
