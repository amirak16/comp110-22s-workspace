"""Building dict test functions."""

__author__ = "730485037"


from dictionary import invert
from dictionary import favorite_color
from dictionary import count


def test_invert_first() -> None:
    """To test invert function."""
    a_first: dict[str, str] = {'a': 'z', 'b': 'y', 'c': 'x'}
    assert invert(a_first) == {'z': 'a', 'y': 'b', 'x': 'c'}
    

def test_invert_sec() -> None:
    """To test invert function."""
    a_first: dict[str, str] = {'h': 'e', 'l': 'o', 'w': 'x'}
    assert invert(a_first) == {'e': 'h', 'o': 'l', 'x': 'w'}


def test_invert_edge() -> None:
    """To test invert function."""
    a_first: dict[str, str] = {}
    assert invert(a_first) == {}


def test_favortie_color_first() -> None:
    """To test favorite color function."""
    b_sec: dict[str, str] = {"Marc": "yellow", "Ezri": "blue", "Kris": "blue"}
    assert favorite_color(b_sec) == "blue"


def test_favortie_color_sec() -> None:
    """To test favorite color function."""
    b_sec: dict[str, str] = {"Lary": "yellow", "Eden": "green", "Max": "purple", "Andy": "yellow"}
    assert favorite_color(b_sec) == "yellow"


def test_favortie_color_edge() -> None:
    """To test favorite color function."""
    b_sec: dict[str, str] = {}
    assert favorite_color(b_sec) == ""


def test_count_first() -> None:
    """To test count function."""
    s: list[str] = ["a", "m", "i", "i", "k"]
    assert count(s) == {"a": 1, "m": 1, "i": 2, "k": 1}


def test_count_sec() -> None:
    """To test count function."""
    s: list[str] = ["dolly", "molly"]
    assert count(s) == {"d": 1, "o": 2, "l": 4, "y": 2, "m": 1}


def test_count_edge() -> None:
    """To test count function."""
    s: list[str] = []
    assert count(s) == {}
