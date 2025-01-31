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

    current_words = [begin]
    next_words = list()

    count = 0
    while current_words:
        count += 1

        for word in words:
            if word in current_words:
                continue

            for current_word in current_words:
                if is_convertable(current_word, word):
                    if word == target:
                        return count

                    next_words.append(word)

        current_words = next_words
        next_words = list()

    return count
