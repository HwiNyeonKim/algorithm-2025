import heapq


def solution(jobs):
    time_consumed = 0

    shortest_job_priority_queue = list()
    time_priority_queue = list()
    for request_time, processing_time in jobs:
        heapq.heappush(time_priority_queue, (request_time, processing_time))

    start_time = 0
    while time_priority_queue:
        request_time, processing_time = heapq.heappop(time_priority_queue)

        if start_time < request_time:
            heapq.heappush(
                time_priority_queue, (request_time, processing_time)
            )

            if not shortest_job_priority_queue:
                start_time = request_time
            else:
                # run processing
                shortest_processing_time, requested_time = heapq.heappop(
                    shortest_job_priority_queue
                )
                end_time = start_time + shortest_processing_time
                time_consumed += end_time - requested_time

                start_time = end_time
        else:
            heapq.heappush(
                shortest_job_priority_queue, (processing_time, request_time)
            )

    while shortest_job_priority_queue:
        shortest_processing_time, requested_time = heapq.heappop(
            shortest_job_priority_queue
        )
        end_time = start_time + shortest_processing_time
        time_consumed += end_time - requested_time

        start_time = end_time

    return time_consumed // len(jobs)
