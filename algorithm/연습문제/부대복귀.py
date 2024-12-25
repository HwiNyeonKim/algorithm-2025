from collections import deque

WALL = 1_000_000


def update_distance(route, origin, destination, distance):
    route[origin][destination] = distance
    route[destination][origin] = distance


def rebuild_route(route, origin):
    destinations = [WALL] * len(route)

    queue = deque([origin])
    while queue:
        current_destination = queue.popleft()
        distance_to_current_destination = route[origin][current_destination]

        for next_destination, distance_from_current_destination in enumerate(
            route[current_destination]
        ):
            if distance_from_current_destination == WALL:
                continue

            distance_to_next_destination = (
                distance_to_current_destination
                + distance_from_current_destination
            )

            if distance_to_next_destination < destinations[next_destination]:
                destinations[next_destination] = distance_to_next_destination
                update_distance(
                    route,
                    origin,
                    next_destination,
                    distance_to_next_destination,
                )
                queue.append(next_destination)


def solution(n, roads, sources, destination):
    # 가정: turn 개념 X -> 부대 겹침 이슈 X
    # - 2 <= len(roads) <= 500,000 -> O(n^2)을 피해야 함

    # 1. Build Map
    route = [
        [WALL for _ in range(n + 1)] for _ in range(n + 1)
    ]  # index 사용 편의성을 위해 0번을 dummy로

    for origin, dest in roads:
        update_distance(route, origin, dest, 1)

    # 2. Rebuild Map with origin(=destination)
    update_distance(route, destination, destination, 0)
    rebuild_route(route, origin=destination)

    return [
        -1
        if route[source][destination] == WALL
        else route[source][destination]
        for source in sources
    ]
