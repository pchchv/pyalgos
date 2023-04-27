"""
Python implementations of a Fixed Priority Queue
and an Element Priority Queue using Python lists.
"""


class OverFlowError(Exception):
    pass


class UnderFlowError(Exception):
    pass


class FixedPriorityQueue:
    """
    Tasks can be added to the priority queue at any time and in any order,
    but when tasks are deleted,
    the task with the highest priority is deleted in FIFO order.
    In the code, we will use three levels of priority,
    with tasks with zero priority being the most urgent (high priority) and
    tasks with priority 2 being the least urgent.
    Examples
    >>> fpq = FixedPriorityQueue()
    >>> fpq.enqueue(0, 10)
    >>> fpq.enqueue(1, 70)
    >>> fpq.enqueue(0, 100)
    >>> fpq.enqueue(2, 1)
    >>> fpq.enqueue(2, 5)
    >>> fpq.enqueue(1, 7)
    >>> fpq.enqueue(2, 4)
    >>> fpq.enqueue(1, 64)
    >>> fpq.enqueue(0, 128)
    >>> print(fpq)
    Priority 0: [10, 100, 128]
    Priority 1: [70, 7, 64]
    Priority 2: [1, 5, 4]
    >>> fpq.dequeue()
    10
    >>> fpq.dequeue()
    100
    >>> fpq.dequeue()
    128
    >>> fpq.dequeue()
    70
    >>> fpq.dequeue()
    7
    >>> print(fpq)
    Priority 0: []
    Priority 1: [64]
    Priority 2: [1, 5, 4]
    >>> fpq.dequeue()
    64
    >>> fpq.dequeue()
    1
    >>> fpq.dequeue()
    5
    >>> fpq.dequeue()
    4
    >>> fpq.dequeue()
    Traceback (most recent call last):
        ...
    data_structures.queue.priority_queue_using_list.UnderFlowError: All queues are empty
    >>> print(fpq)
    Priority 0: []
    Priority 1: []
    Priority 2: []
    """  # noqa: E501

    def __init__(self):
        self.queues = [
            [],
            [],
            [],
        ]

    def enqueue(self, priority: int, data: int) -> None:
        """
        Add an element to a queue based on its priority.
        If the priority is invalid ValueError is raised.
        If the queue is full an OverFlowError is raised.
        """
        try:
            if len(self.queues[priority]) >= 100:
                raise OverflowError("Maximum queue size is 100")
            self.queues[priority].append(data)
        except IndexError:
            raise ValueError("Valid priorities are 0, 1, and 2")

    def dequeue(self) -> int:
        """
        Return the highest priority element in FIFO order.
        If the queue is empty then an under flow exception is raised.
        """
        for queue in self.queues:
            if queue:
                return queue.pop(0)
        raise UnderFlowError("All queues are empty")

    def __str__(self) -> str:
        return "\n".join(f"Priority {i}: {q}" for i,
                         q in enumerate(self.queues))
