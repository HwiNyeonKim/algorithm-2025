import math

'''
Given:
    def solution(progresses, speeds):
        answer = []
        return answer
'''


def solution(progresses, speeds):
    remaining_progresses = [100 - progress for progress in progresses]

    remaining_days = [
        math.ceil(remaining_progress / speed)
        for remaining_progress, speed in zip(remaining_progresses, speeds)
    ]
    remaining_days.append(999_999)  # dummy value

    answer = list()
    count = 1
    current = remaining_days.pop(0)

    while remaining_days:
        next_ = remaining_days.pop(0)

        if current < next_:
            answer.append(count)
            current = next_
            count = 1
        else:
            count += 1

    return answer
