"""
Implementation of a skip lists.
Reference: https://epaperpress.com/sortsearch/download/skiplist.pdf
"""
from __future__ import annotations

from typing import Generic, TypeVar

KT = TypeVar("KT")
VT = TypeVar("VT")


class Node(Generic[KT, VT]):
    def __init__(self, key: KT | str = "root", value: VT | None = None):
        self.key = key
        self.value = value
        self.forward: list[Node[KT, VT]] = []

    def __repr__(self) -> str:
        """
        :return: Visual representation of Node
        >>> node = Node("Key", 2)
        >>> repr(node)
        'Node(Key: 2)'
        """

        return f"Node({self.key}: {self.value})"

    @property
    def level(self) -> int:
        """
        :return: Number of forward references
        >>> node = Node("Key", 2)
        >>> node.level
        0
        >>> node.forward.append(Node("Key2", 4))
        >>> node.level
        1
        >>> node.forward.append(Node("Key3", 6))
        >>> node.level
        2
        """

        return len(self.forward)
