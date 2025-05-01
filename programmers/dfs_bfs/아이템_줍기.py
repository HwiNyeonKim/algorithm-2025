# 사각형들이 존재할 수 있는 범위는 50칸이다. 여기에 계산 편의성을 위해 테두리를 추가(2칸)한다.
# 하지만, 이렇게 설정을 하면 ㄷ자 모양의 경로가 생겼을 때, 꺾지 않고 직진해버리는 문제가 발생할 수 있다.
# 따라서, 위와 같은 경우를 방지하기 위해 사각형의 크기를 2배 스케일링한다. (테두리 추가는 여전히 2칸)
GRID_SIZE = 102


def solution(rectangle, characterX, characterY, itemX, itemY):
    grid = [[0] * GRID_SIZE for _ in range(GRID_SIZE)]
    # GRID_SIZE 선택과 같은 이유로 다른 값들도 2배 스케일링 해준다.
    characterX *= 2
    characterY *= 2
    itemX *= 2
    itemY *= 2
    rectangle = [[value * 2 for value in point] for point in rectangle]

    # * 1. 테두리 경로 탐색
    # * 1.1. 각 사각형의 테두리 포함 내부 전부를 + 1 처리
    # - 테두리만 변경해도 되지만, 감소되는 연산량에 반해 코드 길이만 길어져서 손해인 것 같다.
    for x1, y1, x2, y2 in rectangle:
        for x in range(x1, x2 + 1):
            for y in range(y1, y2 + 1):
                grid[x][y] += 1

    # * 1.2. 각 사각형의 내부를 0으로 설정
    for x1, y1, x2, y2 in rectangle:
        for x in range(x1 + 1, x2):
            for y in range(y1 + 1, y2):
                grid[x][y] = 0

    # * 2. 시작지점에서부터 BFS로 탐색
    location = (characterX, characterY)
    visited = {location}  # set
    queue = [[location, 0, visited]]
    while queue:
        # pop(0)를 하면 O(n)이지만 문제 조건상 이동횟수가 짧으므로 그냥 써본다
        (x, y), move_count, visited = queue.pop(0)

        # 아이템 루팅 성공
        if (x, y) == (itemX, itemY):
            return move_count / 2

        for dx, dy in ((0, -1), (0, 1), (-1, 0), (1, 0)):
            next_x, next_y = x + dx, y + dy

            # 유효한 이동경로(테두리)가 아니면 스킵
            if grid[next_x][next_y] < 1:
                continue

            # 이미 지나간 점이면 스킵
            if (next_x, next_y) in visited:
                continue

            next_location = (next_x, next_y)
            next_move_count = move_count + 1
            next_visited = set(visited)
            next_visited.add(next_location)

            queue.append([next_location, next_move_count, next_visited])

    raise Exception("Should Not Reach Here.")
