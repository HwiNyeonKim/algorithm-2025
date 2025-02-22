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
    return ""
