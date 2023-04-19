from __future__ import annotations
from typing import Any, Generic, TypeVar

T = TypeVar("T", bound=bool)


class SkewNode(Generic[T]):
    """
    One node of the skew pile.
    Contains the value and references to two child nodes.
    """

    def __init__(self, value: T) -> None:
        self._value: T = value
        self.left: SkewNode[T] | None = None
        self.right: SkewNode[T] | None = None

    @property
    def value(self) -> T:
        """Return the value of the node."""
        return self._value

    @staticmethod
    def merge(
        root1: SkewNode[T] | None, root2: SkewNode[T] | None
    ) -> SkewNode[T] | None:
        """Merge 2 nodes together."""
        if not root1:
            return root2

        if not root2:
            return root1

        if root1.value > root2.value:
            root1, root2 = root2, root1

        result = root1
        temp = root1.right
        result.right = root1.left
        result.left = SkewNode.merge(temp, root2)

        return result
