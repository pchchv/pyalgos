"""
Implementation of a single-linked list.

Reference:
https://www.geeksforgeeks.org/data-structures/linked-list/singly-linked-list/
"""
from typing import Any


class Node:
    def __init__(self, data: Any):
        """
        Create and initialize Node class instance.
        >>> Node(20)
        Node(20)
        >>> Node("Hello, world!")
        Node(Hello, world!)
        >>> Node(None)
        Node(None)
        >>> Node(True)
        Node(True)
        """
        self.data = data
        self.next = None

    def __repr__(self) -> str:
        """
        Get the string representation of this node.
        >>> Node(10).__repr__()
        'Node(10)'
        """
        return f"Node({self.data})"
