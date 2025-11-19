# filename: same_tree_recursive.py

from typing import Optional, List
from collections import deque


class TreeNode:
    def __init__(self, val: int = 0,
                 left: Optional["TreeNode"] = None,
                 right: Optional["TreeNode"] = None):
        self.val = val
        self.left = left
        self.right = right


def is_same_tree(p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
    """
    Brute force recursive comparison:
    - Both None -> True
    - One None -> False
    - Values differ -> False
    - Otherwise compare left and right subtrees.
    Time:  O(n)
    Space: O(h) call stack (h = tree height)
    """
    # case 1: both empty
    if p is None and q is None:
        return True

    # case 2: structure mismatch
    if p is None or q is None:
        return False

    # case 3: value mismatch
    if p.val != q.val:
        return False

    # case 4: recursively compare children
    return is_same_tree(p.left, q.left) and is_same_tree(p.right, q.right)


# --- Helpers & quick test (optional) ---

def build_tree_level_order(values: List[Optional[int]]) -> Optional[TreeNode]:
    """
    Build a binary tree from level-order list representation.
    Example: [1, 2, 3, None, 4]
    """
    if not values:
        return None

    root = TreeNode(values[0])
    queue = deque([root])
    i = 1

    while queue and i < len(values):
        node = queue.popleft()

        # left child
        if i < len(values) and values[i] is not None:
            node.left = TreeNode(values[i])
            queue.append(node.left)
        i += 1

        # right child
        if i < len(values) and values[i] is not None:
            node.right = TreeNode(values[i])
            queue.append(node.right)
        i += 1

    return root


if __name__ == "__main__":
    # Example 1
    p = build_tree_level_order([1, 2, 3])
    q = build_tree_level_order([1, 2, 3])
    print(is_same_tree(p, q))  # True

    # Example 2
    p = build_tree_level_order([4, 7])
    q = build_tree_level_order([4, None, 7])
    print(is_same_tree(p, q))  # False

    # Example 3
    p = build_tree_level_order([1, 2, 3])
    q = build_tree_level_order([1, 3, 2])
    print(is_same_tree(p, q))  # False
