def solution(citations):
    citations.sort(reverse=True)

    for h_index, citation in enumerate(citations, start=1):
        if citation < h_index:
            # 마지막으로 성립한 H-Index를 반환
            return h_index - 1

    return h_index
