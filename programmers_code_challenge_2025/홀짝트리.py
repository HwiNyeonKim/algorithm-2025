from collections import defaultdict, deque


def calc_tree_types(queue, remaining_nodes, connections):
    # 값이 홀/짝인 노드
    odd_value_nodes = set()
    even_value_nodes = set()

    # 연결된 노드의 갯수가 홀/짝인 노드
    odd_neighbors = set()
    even_neighbors = set()

    while queue:
        node = queue.popleft()
        if node in odd_value_nodes or node in even_value_nodes:
            continue

        if node % 2 != 0:
            odd_value_nodes.add(node)
        else:
            even_value_nodes.add(node)

        neighbors = connections[node]
        if len(neighbors) % 2 != 0:
            odd_neighbors.add(node)
        else:
            even_neighbors.add(node)

        for n in neighbors:
            queue.append(n)

    # Check odd/even
    odd = odd_value_nodes & odd_neighbors
    even = even_value_nodes & even_neighbors

    # Check reversed odd/even
    reversed_odd = odd_value_nodes & even_neighbors
    reversed_even = even_value_nodes & odd_neighbors

    # Check checked nodes
    remaining_nodes -= odd_value_nodes | even_value_nodes

    return [
        1 if len(odd) + len(even) == 1 else 0,  # 홀짝 트리
        1 if len(reversed_odd) + len(reversed_even) == 1 else 0,  # 역홀짝트리
    ]


def solution(nodes, edges):
    connections = defaultdict(set)
    for edge in edges:
        left, right = edge
        connections[left].add(right)
        connections[right].add(left)

    answer = [0, 0]  # 홀짝트리, 역홀짝트리
    remaining_nodes = set(nodes)
    while remaining_nodes:
        queue = deque([remaining_nodes.pop()])
        count_odd_even, count_reversed = calc_tree_types(
            queue, remaining_nodes, connections
        )
        answer[0] += count_odd_even
        answer[1] += count_reversed

    return answer
