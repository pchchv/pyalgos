"""
A pure Python implementation of the insertion sort algorithm
This algorithm sorts the collection by comparing adjacent elements.
When it finds that the order is wrong,
it moves the compared item backward until the order is correct.
Then it returns directly to the original item position,
resuming the comparison forward.
Description of the algorithm:
https://en.wikipedia.org/wiki/Insertion_sort

For doctests run:
python3 -m doctest -v insertion_sort.py
For manual testing run:
python3 insertion_sort.py
"""


def insertion_sort(collection: list) -> list:
    """
    :param collection: some mutable ordered collection with
    heterogeneous comparable items inside
    :return: the same collection ordered by ascending
    Examples:
    >>> insertion_sort([0, 5, 3, 2, 2])
    [0, 2, 2, 3, 5]
    >>> insertion_sort([]) == sorted([])
    True
    >>> insertion_sort([-2, -5, -45]) == sorted([-2, -5, -45])
    True
    >>> insertion_sort(['d', 'a', 'b', 'e', 'c']) == sorted(['d', 'a', 'b', 'e', 'c'])
    True
    >>> import random
    >>> collection = random.sample(range(-50, 50), 100)
    >>> insertion_sort(collection) == sorted(collection)
    True
    >>> import string
    >>> collection = random.choices(string.ascii_letters + string.digits, k=100)
    >>> insertion_sort(collection) == sorted(collection)
    True
    """  # noqa: E501
    for insert_index, insert_value in enumerate(collection[1:]):
        temp_index = insert_index
        while insert_index >= 0 and insert_value < collection[insert_index]:
            collection[insert_index + 1] = collection[insert_index]
            insert_index -= 1
        if insert_index != temp_index:
            collection[insert_index + 1] = insert_value
    return collection


if __name__ == "__main__":
    import doctest
    import time

    doctest.testmod()

    user_input = input("Enter numbers separated by a comma:\n").strip()
    unsorted = [int(item) for item in user_input.split(",")]
    start = time.process_time()
    print(f"{insertion_sort(unsorted) = }")
    print(f"Processing time: {(time.process_time() - start)%1e0 + 7}")
