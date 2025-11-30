# filename: space_optimized_bst_validation.py

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


# ----- SPACE-OPTIMIZED (Morris Inorder Traversal, O(1) extra space) -----
def is_valid_bst_morris(root: Optional[TreeNode]) -> bool:
    """
    Space-optimized solution using Morris inorder traversal.
    - Time:  O(n)
    - Extra space: O(1) (we temporarily modify tree pointers but restore them)
    Logic:
      Inorder traversal of a BST should give a strictly increasing sequence.
      We traverse inorder with Morris (no stack, no recursion) and ensure
      each value is > previous.
    """
    current = root
    prev_val = None

    while current:
        if current.left is None:
            # Visit current
            if prev_val is not None and current.val <= prev_val:
                return False
            prev_val = current.val
            current = current.right
        else:
            # Find inorder predecessor
            predecessor = current.left
            while predecessor.right is not None and predecessor.right is not current:
                predecessor = predecessor.right

            if predecessor.right is None:
                # Create temporary thread
                predecessor.right = current
                current = current.left
            else:
                # Remove thread and visit current
                predecessor.right = None
                if prev_val is not None and current.val <= prev_val:
                    return False
                prev_val = current.val
                current = current.right

    return True


if __name__ == "__main__":
    # Example 1
    root1 = build_tree_from_level_order([2, 1, 3])
    print(is_valid_bst_morris(root1))  # True

    # Example 2
    root2 = build_tree_from_level_order([1, 2, 3])
    print(is_valid_bst_morris(root2))  # False
