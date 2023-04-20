from __future__ import annotations

from typing import Any


class Node:
    def __init__(self, data: Any):
        self.data: Any = data
        self.next: Node | None = None
