import json
from typing import List, Self


class TreeNode:
    def __init__(self, value=None):
        self.value = value
        self.left = None
        self.right = None

    @property
    def is_leaf(self) -> bool:
        return self.left is None and self.right is None

    def reset_with(self, value):
        self.value = value
        self.left = None
        self.right = None

    @property
    def children(self) -> List[Self]:
        return [self.left, self.right]

    @property
    def children_values(self) -> List:
        return [self.left.value, self.right.value]

    def __str__(self):
        return json.dumps(self.__dict__(), indent=2)

    def __dict__(self):
        return {
            "value": self.value.__dict__() if self.value and hasattr(self.value, "__dict__") else self.value,
            "left": self.left.__dict__() if self.left else None,
            "right": self.right.__dict__() if self.right else None,
        }
