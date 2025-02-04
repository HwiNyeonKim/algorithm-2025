import heapq
from collections import defaultdict


def solution(operations):
    min_heap = list()
    max_heap = list()
    element_counter = defaultdict(int)
    counter = 0

    def pop(heap, sign):
        nonlocal counter

        while heap and element_counter[sign * heap[0]] == 0:
            heapq.heappop(heap)

        value = 0
        if heap:
            value = sign * heapq.heappop(heap)
            element_counter[value] -= 1
            counter -= 1

        return value

    for operation in operations:
        if operation.startswith("I"):
            value = int(operation.split()[1])

            heapq.heappush(min_heap, value)
            heapq.heappush(max_heap, -value)
            element_counter[value] += 1
            counter += 1

        elif operation == "D 1":
            # Pop maximum
            pop(max_heap, -1)

        elif operation == "D -1":
            # Pop minimum
            pop(min_heap, 1)

        else:
            # should not reach here
            raise Exception

        if counter == 0:
            max_heap = list()
            min_heap = list()

    maximum = pop(max_heap, -1)
    element_counter[maximum] += 1
    minimum = pop(min_heap, 1)

    return [maximum, minimum]
