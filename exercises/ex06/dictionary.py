"""Creating dictionary fucntions."""

__author__ = "730485037"


def invert(a_first: dict[str, str]) -> dict[str, str]:
    """It is suppose to invert the kerys and the value of the given dictionary."""
    a_inv: dict[str, str] = {}
    b_key: list[str] = []
    i: int = 0
    for key in a_first:
        b_key.append(key)
    for key in a_first:
        count: int = 0
        for x in b_key:
            if a_first[key] == a_first[x]:
                count += 1
            else:
                i += 1
            if count > 1:
                raise KeyError
            a_inv[a_first[key]] = key
    return a_inv


def favorite_color(b_sec: dict[str, str]) -> str:
    """It should return the favorite color."""
    a_val: dict[str, int] = {}
    for e in b_sec:
        if b_sec[e] in a_val:
            a_val[b_sec[e]] += 1
        else: 
            a_val[b_sec[e]] = 1
    b_y: int = 0
    b_x: str = ""
    for c in a_val:
        if b_y < a_val[c]:
            b_y = a_val[c]
            b_x = c
    return b_x


def count(s: list[str]) -> dict[str, int]:
    """This is a fucntion that counts the number of times a value shows up."""
    none: dict[str, int] = {}
    for b in s:
        if b in none:
            none[b] += 1
        else:
            none[b] = 1
    return none
            