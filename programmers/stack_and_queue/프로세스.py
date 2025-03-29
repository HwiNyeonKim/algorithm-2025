"""
Given:
    def solution(proirities, location):
        answer = 0
        return answer
"""


def solution(priorities, location):
    class Process:
        def __init__(self, priority, isTarget=False):
            self.priority = priority
            self.isTarget = isTarget

    processes = [Process(priority) for priority in priorities]
    processes[location].isTarget = True

    sorted_priorities = sorted(priorities)

    count = 0
    while processes:
        highest_priority = sorted_priorities[-1]
        process = processes.pop(0)

        if process.priority == highest_priority:
            count += 1
            sorted_priorities.pop()

            if process.isTarget:
                return count
        else:
            processes.append(process)

    # Should not reach here
