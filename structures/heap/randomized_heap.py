"""
Implementation of the randomized Heap.
Reference: https://en.wikipedia.org/wiki/Randomized_meldable_heap
"""

from __future__ import annotations

import random
from typing import Generic, TypeVar

T = TypeVar("T", bound=bool)


class RandomizedHeapNode(Generic[T]):
    """
    One node of the randomized heap.
    Contains the value and references to two children.
    """

    def __init__(self, value: T) -> None:
        self._value: T = value
        self.left: RandomizedHeapNode[T] | None = None
        self.right: RandomizedHeapNode[T] | None = None

    @property
    def value(self) -> T:
        """Return the value of the node."""
        return self._value

    @staticmethod
    def merge(
        root1: RandomizedHeapNode[T] | None,
        root2: RandomizedHeapNode[T] | None
    ) -> RandomizedHeapNode[T] | None:
        """Merge 2 nodes."""
        if not root1:
            return root2

        if not root2:
            return root1

        if root1.value > root2.value:
            root1, root2 = root2, root1

        if random.choice([True, False]):
            root1.left, root1.right = root1.right, root1.left

        root1.left = RandomizedHeapNode.merge(root1.left, root2)

        return root1
