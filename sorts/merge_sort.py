"""
Pure Python implementation of the merge sorting algorithm.

For doctests run:
python -m doctest -v merge_sort.py
or
python3 -m doctest -v merge_sort.py
For manual testing, run:
python merge_sort.py
"""


def merge_sort(collection: list) -> list:
    """
   :param collection: some variable ordered collection with
   heterogeneous comparable items inside
   :return: the same collection ordered in ascending order
    Examples:
    >>> merge_sort([0, 5, 3, 2, 2])
    [0, 2, 2, 3, 5]
    >>> merge_sort([])
    []
    >>> merge_sort([-2, -5, -45])
    [-45, -5, -2]
    """

    def merge(left: list, right: list) -> list:
        """
        Merge left and right.
        :param left: left collection
        :param right: right collection
        :return: merge result
        """

        def _merge():
            while left and right:
                yield (left if left[0] <= right[0] else right).pop(0)
            yield from left
            yield from right

        return list(_merge())

    if len(collection) <= 1:
        return collection
    mid = len(collection) // 2
    return merge(merge_sort(collection[:mid]), merge_sort(collection[mid:]))


if __name__ == "__main__":
    import doctest
    import time

    doctest.testmod()

    user_input = input("Enter numbers separated by a comma:\n").strip()
    unsorted = [int(item) for item in user_input.split(",")]
    start = time.process_time()
    print(*merge_sort(unsorted), sep=",")
    print(f"Processing time: {(time.process_time() - start)%1e0 + 7}")
