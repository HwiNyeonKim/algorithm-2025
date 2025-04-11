def count_and_say(n):
    """
    - https://leetcode.com/problems/count-and-say/description/

    Args:
        n (int): 1 <= n <= 30
    Returns:
        string
    """
    results = ["1"]

    while len(results) < n:
        prev = results[-1]

        run_length_encoding = ""
        queue = list()
        for char in list(prev):
            if not queue:
                queue.append(char)
                continue

            peek = queue[-1]
            if char == peek:
                queue.append(peek)
                continue

            run_length_encoding += f"{len(queue)}{peek}"
            queue = [char]

        if queue:
            run_length_encoding += f"{len(queue)}{queue[-1]}"

        results.append(run_length_encoding)

    return results[n - 1]
