from utils.function import add

def count_word(s: str, char: str) -> int:
    assert isinstance(s, str)
    assert isinstance(char, str)
    assert len(char) == 1
    count = 0
    for ch in s:
        if ch == char:
            count = add(count, 1)
    return count