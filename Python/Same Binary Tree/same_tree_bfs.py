# filename: same_tree_bfs.py

from typing import Optional, List
from collections import deque


class TreeNode:
    def __init__(self, val: int = 0,
                 left: Optional["TreeNode"] = None,
                 right: Optional["TreeNode"] = None):
        self.val = val
        self.left = left
        self.right = right


def is_same_tree_bfs(p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
    """
    Iterative BFS using a queue of node pairs (level-order traversal).
    Time:  O(n)
    Space: O(w) where w is max width of the tree.
    """
    queue = deque([(p, q)])

    while queue:
        node_p, node_q = queue.popleft()

        if node_p is None and node_q is None:
            continue

        if node_p is None or node_q is None:
            return False

        if node_p.val != node_q.val:
            return False

        queue.append((node_p.left, node_q.left))
        queue.append((node_p.right, node_q.right))

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
    print(is_same_tree_bfs(p, q))  # True

    p = build_tree_level_order([4, 7])
    q = build_tree_level_order([4, None, 7])
    print(is_same_tree_bfs(p, q))  # False

    p = build_tree_level_order([1, 2, 3])
    q = build_tree_level_order([1, 3, 2])
    print(is_same_tree_bfs(p, q))  # False
