import heapq

WALL = 1_000_000


def dijkstra(n, distance_graph, origin):
    # Destination -> source로 탐색
    distances = [WALL] * (n + 1)  # origin에서 각 지역으로의 최단거리 저장
    distances[origin] = 0

    # [(origin으로부터의 거리, 해당 지역), ...]
    priority_queue = [(0, origin)]

    while priority_queue:
        # origin에서 가장 가까운 지역부터 담색
        distance_from_origin, current_destination = heapq.heappop(
            priority_queue
        )

        # 이미 더 짧은 경로가 파악되었다면, 이 경로는 더이상 계산하지 않는다
        if distance_from_origin > distances[current_destination]:
            continue

        for (
            next_destination,
            distance_to_next_destination_from_current_destination,
        ) in distance_graph[current_destination]:
            distance_to_next_destination_from_origin = (
                distance_from_origin
                + distance_to_next_destination_from_current_destination
            )

            if (
                distance_to_next_destination_from_origin
                < distances[next_destination]
            ):
                distances[next_destination] = (
                    distance_to_next_destination_from_origin
                )
                heapq.heappush(
                    priority_queue,
                    (
                        distance_to_next_destination_from_origin,
                        next_destination,
                    ),
                )

    return distances


def solution(n, roads, sources, destination):
    # 1. Build Initial Graph
    # index 사용 편의성을 위해 0번을 dummy로

    # 각 지역에서 연결된 지역과의 거리를 저장
    # index 사용의 편의성을 위해 index 0 은 dummy로 설정
    distance_graph = [list() for _ in range(n + 1)]

    # 2. Initial Setup
    for start, end in roads:
        distance_graph[start].append((end, 1))
        distance_graph[end].append((start, 1))

    final_distances = dijkstra(n, distance_graph, destination)

    return [
        -1 if final_distances[source] == WALL else final_distances[source]
        for source in sources
    ]
