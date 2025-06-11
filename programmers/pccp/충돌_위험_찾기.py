BOARD_SIZE = 101


def solution(points, routes):
    # 1-base to 0-base
    for i, (r, c) in enumerate(points):
        # element in points: (r, c) on board
        points[i] = (r - 1, c - 1)

    for i, route in enumerate(routes):
        # element in route: index for points
        routes[i] = [r - 1 for r in route]

    # Board setting
    board = [[0] * BOARD_SIZE for _ in range(BOARD_SIZE)]

    # 1. 로봇 초기 배치
    current_locations = list()
    for i, route in enumerate(routes):
        start_index = route[0]
        r, c = points[start_index]
        board[r][c] += 1
        current_locations.append(
            (r, c, route[1:])
        )  # (현재 r, 현재 c, 남은 경로)

    # 초기 배치 상태에서 이미 충돌 가능성이 있다.
    collision_count = len(
        {(r, c) for r, c, _ in current_locations if board[r][c] > 1}
    )

    # 2. 로봇 이동 시작. 이동은 r 방향 먼저, c 방향을 나중에 하되 한번에 한 칸씩만 이동한다.
    while current_locations:
        next_locations = list()
        for r, c, route in current_locations:
            if not route:
                # 이미 최종 목적지까지 이동을 완료했으면, 그 다음 턴에는 board에서 사라진다.
                board[r][c] -= 1
                continue

            # leave current location
            board[r][c] -= 1

            # move to next location
            dest_r, dest_c = points[route[0]]
            if r != dest_r:  # r 방향을 먼저 이동한다.
                r += 1 if r < dest_r else -1
            else:
                c += 1 if c < dest_c else -1
            board[r][c] += 1

            next_locations.append((r, c, route))

            # 미리 지정된 목적지에 도달하였으면, 해당 위치를 목적지 리스트에서 제거한다.
            if r == dest_r and c == dest_c:
                route.pop(0)

        # 이번 턴 이동 후 충돌 가능성이 있는 위치를 찾는다.
        collision_locations = set()
        for r, c, _ in next_locations:
            if board[r][c] > 1:
                collision_locations.add((r, c))

        collision_count += len(collision_locations)

        # update robot positions
        current_locations = next_locations

    return collision_count
