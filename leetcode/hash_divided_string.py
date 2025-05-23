def string_hash(s: str, k: int) -> str:
    n = len(s)
    substrings = [s[i : i + k] for i in range(0, n - k + 1, k)]

    result = ""
    for substring in substrings:
        hash_value_sum = 0
        for char in substring:
            hash_value_sum += ord(char) - ord("a")

        remainder = hash_value_sum % 26
        result += chr(remainder + ord("a"))

    return result
