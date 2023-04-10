"""
A pure Python implementation of a quick sort algorithm.
Description of the algorithm:
https://en.wikipedia.org/wiki/Quicksort

For doctests, run:
python3 -m doctest -v quick_sort.py
For manual testing, run:
python3 quick_sort.py
"""
from __future__ import annotations

from random import randrange


def quick_sort(collection: list) -> list:
    """
    :param collection: a mutable collection of comparable items
    :return: the same collection ordered by ascending
    Examples:
    >>> quick_sort([0, 5, 3, 2, 2])
    [0, 2, 2, 3, 5]
    >>> quick_sort([])
    []
    >>> quick_sort([-2, 5, 0, -45])
    [-45, -2, 0, 5]
    """
    if len(collection) < 2:
        return collection
    pivot_index = randrange(len(collection))  # Use random element as pivot
    pivot = collection[pivot_index]
    greater: list[int] = []  # All elements greater than pivot
    lesser: list[int] = []  # All elements less than or equal to pivot

    for element in collection[:pivot_index]:
        (greater if element > pivot else lesser).append(element)

    for element in collection[pivot_index + 1:]:
        (greater if element > pivot else lesser).append(element)

    return [*quick_sort(lesser), pivot, *quick_sort(greater)]


if __name__ == "__main__":
    import doctest
    import time

    doctest.testmod()

    user_input = input("Enter numbers separated by a comma:\n").strip()
    unsorted = [int(item) for item in user_input.split(",")]
    start = time.process_time()
    print(quick_sort(unsorted))
    print(f"Processing time: {(time.process_time() - start)%1e0 + 7}")
