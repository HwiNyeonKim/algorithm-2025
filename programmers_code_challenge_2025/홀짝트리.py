from collections import defaultdict
from enum import Enum


class NodeType(Enum):
    ODD_EVEN = 0
    REVERSED = 1


class TreeType(Enum):
    ODD_EVEN = 0
    REVERSED = 1
    NONE = 2


tree_types = (TreeType.ODD_EVEN, TreeType.REVERSED, TreeType.NONE)


def get_tree_type(node, connections, root_node_type, node_type_if_not_root):
    # TODO: DFS? deque로 변환하는 로드를 줄여야 할 지도.
    children = connections[node] - set([node])
    visited = set([node])
    while children:
        if any(
            node_type_if_not_root[child] != root_node_type
            for child in children
        ):
            return TreeType.NONE

        visited |= children

        next_children = set()
        for child in children:
            next_children |= connections[child]

        children = next_children - visited

    return tree_types[root_node_type.value]


def solution(nodes, edges):
    connections = defaultdict(set)
    for edge in edges:
        left, right = edge
        connections[left].add(right)
        connections[right].add(left)

    node_type_if_root = dict()
    node_type_if_not_root = dict()
    for node in nodes:
        children = connections[node]
        if node % 2 == len(children) % 2:
            node_type_if_root[node] = NodeType.ODD_EVEN
            node_type_if_not_root[node] = NodeType.REVERSED
        else:
            node_type_if_root[node] = NodeType.REVERSED
            node_type_if_not_root[node] = NodeType.ODD_EVEN

    answer = [0, 0, 0]  # 홀짝트리, 역홀짝트리, 타입없음
    for node in nodes:
        root_node_type = node_type_if_root[node]
        tree_type = get_tree_type(
            node, connections, root_node_type, node_type_if_not_root
        )
        answer[tree_type.value] += 1

    return answer[:2]
