from enum import Enum


class Node:
    def __init__(self, value):
        self.value = value
        self.connected = set()


class TreeType(Enum):
    ODD_EVEN = 0  # 홀짝 트리
    REVERSED = 1  # 역홀짝 트리
    NONE = 2  # 트리 타입 없음


tree_types = dict()  # key: (current node, parent node), value: TreeType


def get_tree_type(node, parent):
    children = node.connected - set([parent])

    if (node, parent) not in tree_types:
        # 현재 노드가 (역)홀수/짝수 노드이고,
        # 이 노드의 각 children을 root로 하는 subtree가 모두 (역)홀짝 트리이면
        # tree_type[(node, parent)]는 (역)홀짝 트리이다.
        if node.value % 2 == len(children) % 2:  # odd/even node
            if all(
                get_tree_type(child, node) == TreeType.ODD_EVEN
                for child in children
            ):
                tree_types[(node, parent)] = TreeType.ODD_EVEN
            else:
                tree_types[(node, parent)] = TreeType.NONE
        else:  # reversed odd/even node
            if all(
                get_tree_type(child, node) == TreeType.REVERSED
                for child in children
            ):
                tree_types[(node, parent)] = TreeType.REVERSED
            else:
                tree_types[(node, parent)] = TreeType.NONE

    return tree_types[(node, parent)]


def solution(nodes, edges):
    """
    문제의 제약조건에 의해 O(n^2)가 되면 시간초과가 예상된다.
    - (역)홀짝 트리의 갯수를 알기 위해서는 일단 모든 node를 한 차례는 순회하며 해당여부를 판단해야 한다.
    - 하지만, 매번 전체 forest를 다시 탐색한다면 O(n^2)이 되어 시간초과이다.
    ! Cycle은 없다고 가정하고 풀이를 진행 해 본다.
    """
    # Forest setup
    forest = dict()
    for node in nodes:
        forest[node] = Node(node)

    for edge in edges:
        left, right = edge
        forest[left].connected.add(forest[right])
        forest[right].connected.add(forest[left])

    # Solve
    answer = [0, 0, 0]
    dummy = Node(0)
    for n in forest.values():
        tree_type = get_tree_type(n, dummy)
        answer[tree_type.value] += 1

    return answer[:2]
