import heapq
from collections import defaultdict


def pop(heap, element_counter, sign):
    while heap and element_counter[sign * heap[0]] == 0:
        heapq.heappop(heap)

    value = 0
    if heap:
        value = sign * heapq.heappop(heap)
        element_counter[value] -= 1

    return value


def solution(operations):
    min_heap = list()
    max_heap = list()
    element_counter = defaultdict(int)

    for operation in operations:
        if operation.startswith("I"):
            value = int(operation.split()[1])

            heapq.heappush(min_heap, value)
            heapq.heappush(max_heap, -value)
            element_counter[value] += 1

        elif operation == "D 1":
            # Pop maximum
            pop(max_heap, element_counter, -1)

        elif operation == "D -1":
            # Pop minimum
            pop(min_heap, element_counter, 1)

        else:
            # should not reach here
            raise Exception

    maximum = pop(max_heap, element_counter, -1)
    element_counter[maximum] += 1
    minimum = pop(min_heap, element_counter, 1)

    return [maximum, minimum]
