"""
- A linked list is like an array; it stores values. However, links in
    a linked list have no indexes.
- This is an example of a double linked list.
- Each link refers to the next link and the previous link.
- A double linked list (DLL) contains an additional pointer,
    usually called the previous pointer.
    Pointer, along with the next pointer and
    the data that is in the single linked list.
- Advantages over SLL - it can be viewed both forward and backward.
    The delete operation is more efficient.

Reference: https://en.wikipedia.org/wiki/Doubly_linked_list
"""


class Node:
    def __init__(self, data: int, previous=None, next_node=None):
        self.data = data
        self.previous = previous
        self.next = next_node

    def __str__(self) -> str:
        return f"{self.data}"

    def get_data(self) -> int:
        return self.data

    def get_next(self):
        return self.next

    def get_previous(self):
        return self.previous


class LinkedListIterator:
    def __init__(self, head):
        self.current = head

    def __iter__(self):
        return self

    def __next__(self):
        if not self.current:
            raise StopIteration
        else:
            value = self.current.get_data()
            self.current = self.current.get_next()
            return value
