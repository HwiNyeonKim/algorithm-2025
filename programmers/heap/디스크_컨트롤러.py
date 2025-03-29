import heapq


def solution(jobs):
    job_queue = sorted(jobs)
    priority_queue = list()
    current_time = 0
    time_consumed = 0

    def _handle_task():
        nonlocal current_time, time_consumed
        processing_time, request_time = heapq.heappop(priority_queue)
        current_time += processing_time
        time_consumed += current_time - request_time

    while job_queue:
        # 1. 현재까지 도착한 작업들을 전부 priority queue에 넣는다.
        while job_queue and job_queue[0][0] <= current_time:
            request_time, processing_time = job_queue.pop(0)
            heapq.heappush(priority_queue, (processing_time, request_time))

        # 2. priority queue에서 가장 짧은 작업을 꺼내서 처리한다.
        if priority_queue:
            _handle_task()
        else:
            # 대기중인 작업이 없으면 다음번 작업까지 점프한다.
            if job_queue:
                current_time = job_queue[0][0]

    # 3. 남은 작업들을 전부 처리한다.
    while priority_queue:
        _handle_task()

    return time_consumed // len(jobs)
