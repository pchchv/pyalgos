"""
Algorithm that merges two sorted linked lists into one sorted linked list.
"""
from __future__ import annotations

from collections.abc import Iterable, Iterator
from dataclasses import dataclass


@dataclass
class Node:
    data: int
    next_node: Node | None


class SortedLinkedList:
    def __init__(self, ints: Iterable[int]) -> None:
        self.head: Node | None = None
        for i in sorted(ints, reverse=True):
            self.head = Node(i, self.head)

    def __iter__(self) -> Iterator[int]:
        """
        >>> tuple(SortedLinkedList(test_data_odd)) == tuple(sorted(test_data_odd))
        True
        >>> tuple(SortedLinkedList(test_data_even)) == tuple(sorted(test_data_even))
        True
        """  # noqa: E501
        node = self.head
        while node:
            yield node.data
            node = node.next_node

    def __len__(self) -> int:
        """
        >>> for i in range(3):
        ...     len(SortedLinkedList(range(i))) == i
        True
        True
        True
        >>> len(SortedLinkedList(test_data_odd))
        8
        """
        return sum(1 for _ in self)

    def __str__(self) -> str:
        """
        >>> str(SortedLinkedList([]))
        ''
        >>> str(SortedLinkedList(test_data_odd))
        '-11 -> -1 -> 0 -> 1 -> 3 -> 5 -> 7 -> 9'
        >>> str(SortedLinkedList(test_data_even))
        '-2 -> 0 -> 2 -> 3 -> 4 -> 6 -> 8 -> 10'
        """
        return " -> ".join([str(node) for node in self])
