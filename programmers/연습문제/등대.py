from collections import defaultdict


def solution(n, lighthouse):
    """
    Args:
        n (int): 노드(등대)의 갯수. 모든 노드는 연결되어 있다.
        lighthous (List[List[int]]): 서로 연결되어 있는 nodes의 정보(간선). n - 1개의 간선.

    Returns:
        int: 항상 불을 켜야 하는 등대의 최소 갯수
    """
    graph = defaultdict(list)
    for a, b in lighthouse:
        graph[a].append(b)
        graph[b].append(a)

    dp = [
        [0, 0] for _ in range(n + 1)
    ]  # dp[node][0 | 1]: node를 끄는/켜는 경우
    # * node의 불을 끄면, 인접 nodes는 반드시 켜져 있어야 한다.
    # * node의 불을 켜면, 인접 nodes는 켜져 있어도 되고, 꺼져 있어도 된다.
    visited = [False] * (n + 1)

    stack = [(1, -1)]  # 대충 1번 노드를 root로 잡는다.
    order = list()

    while stack:
        node, parent = stack.pop()
        if visited[node]:
            continue

        visited[node] = True
        order.append((node, parent))

        for neighbor in graph[node]:
            if not visited[neighbor]:
                stack.append((neighbor, node))

    while order:
        node, parent = order.pop()
        dp[node][0] = 0
        dp[node][1] = 1

        for child in graph[node]:
            if child == parent:
                continue

            # node의 불을 끄면, child는 켜져있어야 한다
            dp[node][0] += dp[child][1]
            # node의 불을 켜면, 그 child에 대해서는 최소로 키는 경우만 본다.
            dp[node][1] += min(dp[child][0], dp[child][1])

    return min(dp[1][0], dp[1][1])
