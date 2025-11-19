# filename: same_tree_iterative_dfs.py

from typing import Optional, List
from collections import deque


class TreeNode:
    def __init__(self, val: int = 0,
                 left: Optional["TreeNode"] = None,
                 right: Optional["TreeNode"] = None):
        self.val = val
        self.left = left
        self.right = right


def is_same_tree_iterative(p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
    """
    Iterative DFS using a stack of node pairs.
    Time:  O(n)
    Space: O(h) in worst case (stack), same asymptotics as recursion but no call-stack limits.
    """
    stack = [(p, q)]

    while stack:
        node_p, node_q = stack.pop()

        # both None -> this position is fine, continue
        if node_p is None and node_q is None:
            continue

        # exactly one is None -> structure mismatch
        if node_p is None or node_q is None:
            return False

        # value mismatch
        if node_p.val != node_q.val:
            return False

        # push children pairs (right, left) – order doesn't matter as long as it's consistent
        stack.append((node_p.left, node_q.left))
        stack.append((node_p.right, node_q.right))

    return True


# --- Helpers & quick test (optional) ---

def build_tree_level_order(values: List[Optional[int]]) -> Optional[TreeNode]:
    if not values:
        return None

    root = TreeNode(values[0])
    queue = deque([root])
    i = 1

    while queue and i < len(values):
        node = queue.popleft()

        if i < len(values) and values[i] is not None:
            node.left = TreeNode(values[i])
            queue.append(node.left)
        i += 1

        if i < len(values) and values[i] is not None:
            node.right = TreeNode(values[i])
            queue.append(node.right)
        i += 1

    return root


if __name__ == "__main__":
    p = build_tree_level_order([1, 2, 3])
    q = build_tree_level_order([1, 2, 3])
    print(is_same_tree_iterative(p, q))  # True

    p = build_tree_level_order([4, 7])
    q = build_tree_level_order([4, None, 7])
    print(is_same_tree_iterative(p, q))  # False

    p = build_tree_level_order([1, 2, 3])
    q = build_tree_level_order([1, 3, 2])
    print(is_same_tree_iterative(p, q))  # False
