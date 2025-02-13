from collections import defaultdict
from enum import Enum


class TreeType(Enum):
    ODD_EVEN = 0  # 홀짝 트리
    REVERSED = 1  # 역홀짝 트리
    NONE = 2  # 트리 타입 없음


def get_tree_type(node, parent, connections, tree_types):
    stack = [(node, parent)]

    while stack:
        # 현재 노드가 (역)홀수/짝수 노드이고,
        # 이 노드의 각 children을 root로 하는 subtree가 모두 (역)홀짝 트리이면
        # tree_type[(node, parent)]는 (역)홀짝 트리이다.
        current_node, parent_node = stack[-1]
        if (current_node, parent_node) in tree_types:
            stack.pop()
            continue

        children = connections[current_node] - set([parent_node])

        # Leaf Node의 Tree Type을 계산 해 놓는다.
        if len(children) == 0:  # Leaf node
            if current_node % 2 == 0:
                tree_types[(current_node, parent_node)] = TreeType.ODD_EVEN
            else:
                tree_types[(current_node, parent_node)] = TreeType.REVERSED
        else:
            # Leaf Nodes는 모두 타입이 확인되었음을 가정하고, 현 노드와 자식 노드들의 타입을 확인한다.
            if all((child, current_node) in tree_types for child in children):
                stack.pop()
                if current_node % 2 == len(children) % 2:
                    if all(
                        tree_types[(child, current_node)] == TreeType.ODD_EVEN
                        for child in children
                    ):
                        tree_types[(current_node, parent_node)] = (
                            TreeType.ODD_EVEN
                        )
                    else:
                        tree_types[(current_node, parent_node)] = TreeType.NONE
                else:
                    if all(
                        tree_types[(child, current_node)] == TreeType.REVERSED
                        for child in children
                    ):
                        tree_types[(current_node, parent_node)] = (
                            TreeType.REVERSED
                        )
                    else:
                        tree_types[(current_node, parent_node)] = TreeType.NONE
            else:
                # 자식 노드 중 타입이 확인되지 않은 노드가 있다면 stack에 추가한다.
                for child in children:
                    stack.append((child, current_node))

    return tree_types[(node, parent)]


def solution(nodes, edges):
    """
    문제의 제약조건에 의해 O(n^2)가 되면 시간초과가 예상된다.
    - (역)홀짝 트리의 갯수를 알기 위해서는 일단 모든 node를 한 차례는 순회하며 해당여부를 판단해야 한다.
    - 하지만, 매번 전체 forest를 다시 탐색한다면 O(n^2)이 되어 시간초과이다.
    ! Cycle은 없다고 가정하고 풀이를 진행 해 본다.
    """
    connections = defaultdict(set)
    for edge in edges:
        left, right = edge
        connections[left].add(right)
        connections[right].add(left)

    # Solve
    answer = [0, 0, 0]  # 홀짝트리, 역홀짝트리, 타입없음
    dummy = 0
    tree_types = dict()  # key: (current node, parent node), value: TreeType
    for node in nodes:
        tree_type = get_tree_type(node, dummy, connections, tree_types)
        answer[tree_type.value] += 1

    return answer[:2]
