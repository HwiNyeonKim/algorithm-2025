def solution(info, edges):
    # BFS로 leaf 노드들을 추가한 케이스를 확인한다. 늑대 >= 양인 경우는 pruning
    edges.sort()
    queue = list()  # element: [node: int, leafs: list, sheep: int, wolf: int]

    # 다음으로 선택 가능한 노드들. 현재까지 선택한 모든 노드들의 자식 노드
    leaf_nodes = list()
    # 전체 트리에 대해서는 leaf nodes가 아니지만,
    # root에서부터 직접 이동해가며 탐색완료한 트리를 넓혀간다는 의미에서 leaf nodes로 표현

    # 초기 셋업
    for edge in edges:
        if edge[0] != 0:
            break

        leaf_nodes.append(edge[1])

    queue.append([leaf_nodes, 1, 0])  # root

    # 탐색중인 트리의 leaf nodes를 BFS로 탐색해가며 케이스 확인
    answer = list()  # 각 케이스별 최종적으로 모은 양의 수
    while queue:
        leafs, sheep, wolf = queue.pop(0)

        if not leafs:  # 탐색 완료
            answer.append(sheep)

        for leaf in leafs:  # leaf: 다음번 선택
            # leaf를 선택했을 때, 변화하는 늑대와 양의 수 확인
            next_sheep, next_wolf = sheep, wolf
            if info[leaf] == 0:
                next_sheep += 1
            else:
                next_wolf += 1

            if next_wolf >= next_sheep:
                # 더이상 진행 불가. 사실상 탐색 완료
                answer.append(
                    next_sheep
                )  # 이곳에서는 sheep = next_sheep 이다.
                continue

            # leaf를 선택했을 때, 다음번 선택할 수 있는 leaf 노드들을 추가
            next_leafs = list(leafs)
            next_leafs.remove(leaf)
            for next_edge in edges:
                # edges의 길이가 충분히 작으므로 그냥 매번 중복해서 순회해버린다.
                if next_edge[0] == leaf:
                    next_leafs.append(next_edge[1])

            queue.append([next_leafs, next_sheep, next_wolf])

    return max(answer)
