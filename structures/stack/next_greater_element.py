from __future__ import annotations

arr = [-10, -5, 0, 5, 5.1, 11, 13, 21, 3, 4, -21, -10, -5, -1, 0]
expect = [-5, 0, 5, 5.1, 11, 13, 21, -1, 4, -1, -10, -5, -1, 0, -1]


def next_greatest_element_slow(arr: list[float]) -> list[float]:
    """
    Gets the next greatest element (NGE) for all elemnts in the list.
    The maximum item present after the current one,
    which is also greater than the current one.
    >>> next_greatest_element_slow(arr) == expect
    True
    """

    result = []
    arr_size = len(arr)

    for i in range(arr_size):
        next_element: float = -1
        for j in range(i + 1, arr_size):
            if arr[i] < arr[j]:
                next_element = arr[j]
                break
        result.append(next_element)
    return result


def next_greatest_element_fast(arr: list[float]) -> list[float]:
    """
    Like next_greatest_element_slow() but changes the loops to use
    enumerate() instead of range(len()) for the outer loop and
    for in a slice of arr for the inner loop.
    >>> next_greatest_element_fast(arr) == expect
    True
    """
    result = []
    for i, outer in enumerate(arr):
        next_item: float = -1
        for inner in arr[i + 1:]:
            if outer < inner:
                next_item = inner
                break
        result.append(next_item)
    return result


def next_greatest_element(arr: list[float]) -> list[float]:
    """
    Get the next greatest element (NGE) for all elements in the list.
    The maximal element present after the current one,
    which is also larger than the current one.
    The naive way to solve this problem is to do two loops and
    check that the next element is greater.
    But this would make the time complexity equal to O(n^2).
    A better way to solve it would be to use the stack to keep track of
    the maximum number, which would give a linear solution time.
    >>> next_greatest_element(arr) == expect
    True
    """
    arr_size = len(arr)
    stack: list[float] = []
    result: list[float] = [-1] * arr_size

    for index in reversed(range(arr_size)):
        if stack:
            while stack[-1] <= arr[index]:
                stack.pop()
                if not stack:
                    break
        if stack:
            result[index] = stack[-1]
        stack.append(arr[index])
    return result


if __name__ == "__main__":
    from doctest import testmod
    from timeit import timeit

    testmod()
    print(next_greatest_element_slow(arr))
    print(next_greatest_element_fast(arr))
    print(next_greatest_element(arr))

    setup = (
        "from __main__ import arr, next_greatest_element_slow, "
        "next_greatest_element_fast, next_greatest_element"
    )
    print(
        "next_greatest_element_slow():",
        timeit("next_greatest_element_slow(arr)", setup=setup),
    )
    print(
        "next_greatest_element_fast():",
        timeit("next_greatest_element_fast(arr)", setup=setup),
    )
    print(
        "     next_greatest_element():",
        timeit("next_greatest_element(arr)", setup=setup),
    )
