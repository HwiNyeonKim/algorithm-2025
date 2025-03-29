def solution(n, words):
    answer = [0, 0]
    spoken = set()

    prev_word = words.pop(0)
    spoken.add(prev_word)
    for index, word in enumerate(words, start=1):
        man_number = index % n + 1
        turns = index // n + 1

        if word in spoken or not word.startswith(prev_word[-1]):
            answer = [man_number, turns]
            break

        spoken.add(word)
        prev_word = word

    return answer
