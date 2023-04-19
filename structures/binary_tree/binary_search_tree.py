class Node:
    def __init__(self, value: int | None = None):
        self.value = value
        self.parent: Node | None = None  # Added to simplify node removal
        self.left: Node | None = None
        self.right: Node | None = None

    def __repr__(self) -> str:
        from pprint import pformat

        if self.left is None and self.right is None:
            return str(self.value)
        return pformat({f"{self.value}": (self.left, self.right)}, indent=1)
