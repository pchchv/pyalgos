"""
A pure Python implementation of a exchange sort algorithm.
Description of the algorithm:
https://en.wikipedia.org/wiki/Sorting_algorithm#Exchange_sort

For doctests, run:
python3 -m doctest -v exchange_sort.py
For manual testing, run:
python3 exchange_sort.py
"""


def exchange_sort(numbers: list[int]) -> list[int]:
    """
    :param collection: a mutable collection of comparable items
    :return: the same collection ordered by ascending
    Examples:
    >>> exchange_sort([5, 4, 3, 2, 1])
    [1, 2, 3, 4, 5]
    >>> exchange_sort([-1, -2, -3])
    [-3, -2, -1]
    >>> exchange_sort([1, 2, 3, 4, 5])
    [1, 2, 3, 4, 5]
    >>> exchange_sort([0, 10, -2, 5, 3])
    [-2, 0, 3, 5, 10]
    >>> exchange_sort([])
    []
    """
    numbers_length = len(numbers)
    for i in range(numbers_length):
        for j in range(i + 1, numbers_length):
            if numbers[j] < numbers[i]:
                numbers[i], numbers[j] = numbers[j], numbers[i]
    return numbers


if __name__ == "__main__":
    import doctest
    import time

    doctest.testmod()

    user_input = input("Enter numbers separated by a comma:\n").strip()
    unsorted = [int(item) for item in user_input.split(",")]
    start = time.process_time()
    print(exchange_sort(unsorted))
    print(f"Processing time: {(time.process_time() - start)%1e0 + 7}")
