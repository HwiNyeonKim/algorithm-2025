from heapq import heappop, heappush


def solution(n, works):
    max_heap = list()
    for work in works:
        heappush(max_heap, -work)

    for _ in range(n):
        work = heappop(max_heap)
        if work < 0:
            work += 1
        heappush(max_heap, work)

    return sum(remaining_work**2 for remaining_work in max_heap)
