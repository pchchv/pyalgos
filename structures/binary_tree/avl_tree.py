"""
Implementation of an auto-balanced binary tree!

For doctests run following command:
python3 -m doctest -v avl_tree.py
For testing run:
python avl_tree.py
"""
from __future__ import annotations

from typing import Any


class Queue:
    def __init__(self) -> None:
        self.data: list[Any] = []
        self.head: int = 0
        self.tail: int = 0

    def is_empty(self) -> bool:
        return self.head == self.tail

    def push(self, data: Any) -> None:
        self.data.append(data)
        self.tail = self.tail + 1

    def pop(self) -> Any:
        ret = self.data[self.head]
        self.head = self.head + 1
        return ret

    def count(self) -> int:
        return self.tail - self.head

    def print_queue(self) -> None:
        print(self.data)
        print("**************")
        print(self.data[self.head: self.tail])


class Node:
    def __init__(self, data: Any) -> None:
        self.data = data
        self.left: Node | None = None
        self.right: Node | None = None
        self.height: int = 1

    def get_data(self) -> Any:
        return self.data

    def get_left(self) -> Node | None:
        return self.left

    def get_right(self) -> Node | None:
        return self.right

    def get_height(self) -> int:
        return self.height

    def set_data(self, data: Any) -> None:
        self.data = data

    def set_left(self, node: Node | None) -> None:
        self.left = node

    def set_right(self, node: Node | None) -> None:
        self.right = node

    def set_height(self, height: int) -> None:
        self.height = height
