"""Building a list utility test functions."""


__author__ = "730485037"


from utils import only_evens
from utils import sub
from utils import concat


def test_even_numbers_with_only_even_1() -> None:
    """Test function with only even."""
    xs: list[int] = [2, 4, 6, 8]
    assert only_evens(xs) == [2, 4, 6, 8]
 

def test_even_numbers_2() -> None:
    """Test function with only random numbers."""
    xs: list[int] = [1, 2, 3, 5, 6, 8] 
    assert only_evens(xs) == [2, 6, 8]


def test_even_numbers_with_only_even_edge() -> None:
    """Test function with empty brackets."""
    xs: list[int] = []
    assert only_evens(xs) == []


def test_sub() -> None:
    """Test function with list that ends int -1 random."""
    a_list: list[int] = [1, 2, 3, 5, 6, 8] 
    s_list: int = 1
    e_list: int = 3
    assert sub(a_list, s_list, e_list) == [2, 3]


def test_sub_1() -> None:
    """Test function with list that ends int -1 random 2."""
    a_list: list[int] = [1, 2, 3, 5, 6, 8] 
    s_list: int = 1
    e_list: int = 4
    assert sub(a_list, s_list, e_list) == [2, 3, 5]


def test_sub_edge() -> None:
    """Test function with empty brackets."""
    a_list: list[int] = [] 
    s_list: int = 0
    e_list: int = 0
    assert sub(a_list, s_list, e_list) == []


def test_concat() -> None:
    """Test function with list over list with single digits."""
    one_list: list[int] = [1, 2, 3, 4, 5]
    two_list: list[int] = [6, 7, 8, 9, 10]
    assert concat(one_list, two_list) == [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


def test_concat_1() -> None:
    """Test function with list over list with double digits."""
    one_list: list[int] = [10, 20, 30, 40, 50]
    two_list: list[int] = [60, 70, 80, 90, 100]
    assert concat(one_list, two_list) == [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]


def test_concat_edge() -> None:
    """Test function with empty brackets."""
    one_list: list[int] = []
    two_list: list[int] = []
    assert concat(one_list, two_list) == []
