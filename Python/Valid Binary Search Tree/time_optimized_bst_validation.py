# filename: time_optimized_bst_validation.py

from math import inf
from collections import deque
from typing import Optional, List


class TreeNode:
    def __init__(self, val: int = 0,
                 left: Optional["TreeNode"] = None,
                 right: Optional["TreeNode"] = None):
        self.val = val
        self.left = left
        self.right = right


def build_tree_from_level_order(values: List[Optional[int]]) -> Optional[TreeNode]:
    """Helper to build a binary tree from level-order list representation."""
    if not values:
        return None

    it = iter(values)
    root_val = next(it)
    if root_val is None:
        return None

    root = TreeNode(root_val)
    queue = deque([root])

    for val in it:
        current = queue.popleft()

        # Left child
        left_val = val
        if left_val is not None:
            current.left = TreeNode(left_val)
        queue.append(current.left)

        # Right child (might exhaust iterator)
        try:
            right_val = next(it)
        except StopIteration:
            break

        if right_val is not None:
            current.right = TreeNode(right_val)
        queue.append(current.right)

    return root


# ----- TIME-OPTIMIZED O(n) -----
def is_valid_bst_bounds(root: Optional[TreeNode]) -> bool:
    """
    Optimal time solution:
    DFS with value bounds (min_allowed, max_allowed).
    Time:  O(n) – each node visited once.
    Space: O(h) – recursion stack, h = tree height.
    """

    def dfs(node: Optional[TreeNode], low: float, high: float) -> bool:
        if not node:
            return True

        if not (low < node.val < high):
            return False

        # Left subtree: values must be < node.val
        # Right subtree: values must be > node.val
        return dfs(node.left, low, node.val) and dfs(node.right, node.val, high)

    return dfs(root, -inf, inf)


if __name__ == "__main__":
    # Example 1
    root1 = build_tree_from_level_order([2, 1, 3])
    print(is_valid_bst_bounds(root1))  # True

    # Example 2
    root2 = build_tree_from_level_order([1, 2, 3])
    print(is_valid_bst_bounds(root2))  # False
