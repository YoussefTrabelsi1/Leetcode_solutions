# filename: brute_force_bst_validation.py

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


# ----- BRUTE FORCE O(n^2) -----
def is_valid_bst_bruteforce(root: Optional[TreeNode]) -> bool:
    """
    Brute-force check:
    For each node, recompute max of left subtree and min of right subtree.
    Time:  O(n^2) in worst case (skewed tree).
    Space: O(h) recursion stack.
    """

    def get_min(node: Optional[TreeNode]) -> int:
        if not node:
            return inf
        return min(node.val, get_min(node.left), get_min(node.right))

    def get_max(node: Optional[TreeNode]) -> int:
        if not node:
            return -inf
        return max(node.val, get_max(node.left), get_max(node.right))

    def validate(node: Optional[TreeNode]) -> bool:
        if not node:
            return True

        # Check left subtree max < node.val
        if node.left:
            left_max = get_max(node.left)
            if left_max >= node.val:
                return False

        # Check right subtree min > node.val
        if node.right:
            right_min = get_min(node.right)
            if right_min <= node.val:
                return False

        # Recurse
        return validate(node.left) and validate(node.right)

    return validate(root)


if __name__ == "__main__":
    # Example 1
    root1 = build_tree_from_level_order([2, 1, 3])
    print(is_valid_bst_bruteforce(root1))  # True

    # Example 2
    root2 = build_tree_from_level_order([1, 2, 3])
    print(is_valid_bst_bruteforce(root2))  # False
