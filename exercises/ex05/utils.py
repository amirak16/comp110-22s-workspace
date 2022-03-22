"""Building a list utility function."""
__author__ = "730485037"


def only_evens(number_list: list[int]) -> list[int]:     
    """In a list only the even numbers are supposed to be returned."""
    even_numbers: list[int] = list()
    for item in number_list:
        if item % 2 == 0:
            even_numbers.append(item)
    return even_numbers


def sub(a_list: list[int], s_list: int, e_list: int) -> list[int]:
    """In a list only the subset of the goven list should be returned between the start and end index."""
    subset_numbers: list[int] = []
    i: int = 0
    if s_list < 0:
        s_list = 0
    if e_list > len(a_list):
        e_list = len(a_list)
    if len(a_list) == 0 or s_list > len(a_list) or e_list <= 0:
        return subset_numbers
    i = s_list
    while i < e_list:
        subset_numbers.append(a_list[i])
        i += 1
    return subset_numbers 


def concat(one_list: list[int], two_list: list[int]) -> list[int]:
    """It needs to generate a new list which contains all of the elements of the first list and the second list."""
    another_list = []
    for x in one_list:
        another_list.append(x)
    for x in two_list:
        another_list.append(x)
    return another_list