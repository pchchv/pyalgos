"""
Pure Python implementation of the cycle sorting algorithm.
Description of the algorithm:
https://en.wikipedia.org/wiki/Cycle_sort

For doctests run:
python -m doctest -v cycle_sort.py
or
python3 -m doctest -v cycle_sort.py
For manual testing, run:
python cycle_sort.py
"""


def cycle_sort(array: list) -> list:
    """
    :param collection: some variable ordered collection with
    heterogeneous comparable items inside
    :return: the same collection ordered in ascending order
    Examples:
    >>> cycle_sort([4, 3, 2, 1])
    [1, 2, 3, 4]
    >>> cycle_sort([-4, 20, 0, -50, 100, -1])
    [-50, -4, -1, 0, 20, 100]
    >>> cycle_sort([-.1, -.2, 1.3, -.8])
    [-0.8, -0.2, -0.1, 1.3]
    >>> cycle_sort([])
    []
    """
    array_len = len(array)
    for cycle_start in range(0, array_len - 1):
        item = array[cycle_start]

        pos = cycle_start
        for i in range(cycle_start + 1, array_len):
            if array[i] < item:
                pos += 1

        if pos == cycle_start:
            continue

        while item == array[pos]:
            pos += 1

        array[pos], item = item, array[pos]
        while pos != cycle_start:
            pos = cycle_start
            for i in range(cycle_start + 1, array_len):
                if array[i] < item:
                    pos += 1

            while item == array[pos]:
                pos += 1

            array[pos], item = item, array[pos]

    return array


if __name__ == "__main__":
    import doctest
    import time

    doctest.testmod()

    user_input = input("Enter numbers separated by a comma:\n").strip()
    unsorted = [int(item) for item in user_input.split(",")]
    start = time.process_time()
    print(*cycle_sort(unsorted), sep=",")
    print(f"Processing time: {(time.process_time() - start)%1e0 + 7}")
