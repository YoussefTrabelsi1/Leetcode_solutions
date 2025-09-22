# filename: order_statistic_tree_augmented.py

from typing import List, Optional, Tuple

class TreeNode:
    def __init__(self, val: int = 0, left: "Optional[TreeNode]" = None, right: "Optional[TreeNode]" = None):
        self.val = val
        self.left = left
        self.right = right
        self.size = 1  # subtree size including self (to be corrected by post-order build)

def build_tree(level: List[Optional[int]]) -> Optional[TreeNode]:
    """
    Builds a binary tree from a level-order list (use None for missing nodes).
    After building, computes and attaches 'size' = subtree node count to each node.
    """
    from collections import deque
    if not level:
        return None
    it = iter(level)
    root_val = next(it)
    if root_val is None:
        return None
    root = TreeNode(root_val)
    q = deque([root])
    for left_val, right_val in zip(it, it):
        node = q.popleft()
        if left_val is not None:
            node.left = TreeNode(left_val)
            q.append(node.left)
        if right_val is not None:
            node.right = TreeNode(right_val)
            q.append(node.right)
    remaining = list(it)
    if remaining and q:
        val = remaining[0]
        if val is not None:
            q[0].left = TreeNode(val)

    # Post-order to compute sizes
    def compute_sizes(n: Optional[TreeNode]) -> int:
        if not n:
            return 0
        left_sz = compute_sizes(n.left)
        right_sz = compute_sizes(n.right)
        n.size = 1 + left_sz + right_sz
        return n.size

    compute_sizes(root)
    return root

def kth_smallest(root: Optional[TreeNode], k: int) -> int:
    """
    ORDER-STATISTIC TREE approach (optimal for repeated queries):
    Assumes each node stores subtree size.
    Single query: O(h) time, O(1) extra space after an O(n) preprocessing.
    """
    node = root
    while node:
        left_size = node.left.size if node.left else 0
        if k == left_size + 1:
            return node.val
        elif k <= left_size:
            node = node.left
        else:
            k -= left_size + 1
            node = node.right
    return -1  # k is guaranteed valid

if __name__ == "__main__":
    # Example 1
    root = build_tree([2, 1, 3])
    print(kth_smallest(root, 1))  # Expected: 1

    # Example 2
    root = build_tree([4, 3, 5, 2, None])
    print(kth_smallest(root, 4))  # Expected: 5
