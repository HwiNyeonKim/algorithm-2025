def alphabet_to_int(char: str):
    if len(char) != 1:
        raise Exception

    return ord(char) - ord("a") + 1


def int_to_alphabet(index: int):
    return chr(index + 96)


def get_spell(index: int):
    spell = list()

    while index >= 0:
        if index == 0:
            break

        char_int = (index - 1) % 26
        spell.append(int_to_alphabet(char_int + 1))
        index = (index - 1) // 26

    spell.reverse()
    return "".join(spell)


def get_index(spell: str):
    index = 0
    for power, char in enumerate(spell[::-1]):
        index += alphabet_to_int(char) * 26**power

    return index


def solution(n, bans):
    # 1. index <-> spell 상호 변환 function 정의 및 구현
    # 2. bans -> banned spell의 index 계산
    # 3. n보다 작은 index를 가지는 banned spell의 수 계산
    # 4. func(n + 3의 결과)를 return
    banned_indices = [get_index(ban) for ban in bans]
    banned_indices.sort()
    for banned_index in banned_indices:
        if banned_index <= n:
            n += 1

    return get_spell(n)
