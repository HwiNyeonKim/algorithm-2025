INF = float("inf")


def solution(n, s, a, b, fares):
    """
    Args:
        n (int): 지점의 갯수, [3, 200]
        s (int): 출발지점, [1, n]
        a (int): A의 도착지점, [1, n]
        b (int): B의 도착지점, [1, n]
        fares (List[List[int]]): 지점간 택시요금

    Returns:
        int: s에서 출발하여 A와 B가 각자 도착지점까지 이동하는데 필요한 최소 택시 요금.
                합승은 할 수도 있고, 하지 않을수도 있다.
    """
    # index 계산 편의성을 위해 s, a, b를 0-base로 수정
    s -= 1
    a -= 1
    b -= 1

    # Graph: Initial state
    graph = [[INF] * n for _ in range(n)]

    for from_ in range(n):
        graph[from_][from_] = 0  # 자기 자신으로 가는 비용은 0

    for from_, to, fare in fares:
        graph[from_ - 1][to - 1] = fare
        graph[to - 1][from_ - 1] = fare

    # Floyd-Warshall
    for midpoint in range(n):
        for from_ in range(n):
            for to in range(n):
                graph[from_][to] = min(
                    graph[from_][to],
                    graph[from_][midpoint] + graph[midpoint][to],
                )

    minimum_fare = INF
    for midpoint in range(n):
        minimum_fare = min(
            minimum_fare,
            graph[s][midpoint] + graph[midpoint][a] + graph[midpoint][b],
        )

    return minimum_fare
