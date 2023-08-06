from typing import Callable
from src.core.utils.logger import Logger
from src.core.datastructures.binarytree.node import TreeNode
import json

logger = Logger(__name__)


class BinaryTree:
    def __init__(self, root: TreeNode = None):
        self.root = root or TreeNode()

    @staticmethod
    def of_height(height: int):
        def _build_level(level: int):
            node = TreeNode()
            if level != 0:
                node.left = _build_level(level - 1)
                node.right = _build_level(level - 1)
            return node

        root = _build_level(height)
        return BinaryTree(root)

    def fill_with(self, items: list):
        def _fill(node: TreeNode, items: list):
            if node is None or len(items) == 0:
                return
            node.value = items.pop(0)
            _fill(node.left, items)
            _fill(node.right, items)

        _fill(self.root, items)

    def fill_leaves(self, items: list):
        def _fill(node: TreeNode, items: list):
            if node is None or len(items) == 0:
                return
            if node.is_leaf:
                node.value = items.pop(0)
            _fill(node.left, items)
            _fill(node.right, items)

        _fill(self.root, items)

    def traverse(self, visit: Callable[[TreeNode], None]):
        self._dfs(self.root, visit)

    def _dfs(self, node: TreeNode, visit: Callable[[TreeNode], None]):
        if node is None:
            return
        self._dfs(node.left, visit)
        self._dfs(node.right, visit)
        visit(node)

    def _dfs_to_list(self, node: TreeNode) -> list:
        if node is None:
            return []
        return [
            *self._dfs_to_list(node.left),
            *self._dfs_to_list(node.right),
            node,
        ]

    def size(self):
        def _size(node: TreeNode):
            if node is None:
                return 0
            return 1 + _size(node.left) + _size(node.right)
        return _size(self.root)

    def height(self):
        def _height(node: TreeNode):
            if node is None:
                return 0
            return 1 + max(_height(node.left), _height(node.right))
        return _height(self.root)

    def __str__(self):
        return json.dumps(self.__dict__(), indent=2)

    def __dict__(self):
        return {"tree": self.root.__dict__()}
