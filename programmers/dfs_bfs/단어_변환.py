from collections import deque


def is_convertable(word_from, word_to):
    diff_count = 0
    for char_from, char_to in zip(word_from, word_to):
        if char_from != char_to:
            diff_count += 1

        if diff_count > 1:
            return False

    return True


def solution(begin, target, words):
    if target not in words:
        return 0

    queue = deque([(0, begin)])  # count to change, changed word
    checked = set([begin])

    while queue:
        count, current_word = queue.popleft()

        for word in words:
            if word in checked:
                continue

            if is_convertable(current_word, word):
                if word == target:
                    return count + 1

                queue.append((count + 1, word))
                checked.add(word)

    return 0
