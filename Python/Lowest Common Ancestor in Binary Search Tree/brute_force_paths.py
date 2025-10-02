# Brute-force (general binary tree approach using root-to-node paths)
# Time: O(n), Space: O(n) for storing paths.
# Works for any binary tree; doesn't use BST properties.

from collections import deque
from typing import Optional, List, Any

class TreeNode:
    def __init__(self, val: int = 0,
                 left: Optional['TreeNode'] = None,
                 right: Optional['TreeNode'] = None):
        self.val = val
        self.left = left
        self.right = right

def build_tree_level(values: List[Any]) -> Optional[TreeNode]:
    """Builds a binary tree from a level-order list where None or 'null' denote missing nodes."""
    if not values:
        return None
    vals = [None if (v is None or v == 'null') else v for v in values]
    root = TreeNode(vals[0])
    q = deque([root])
    i = 1
    n = len(vals)
    while q and i < n:
        node = q.popleft()
        if i < n and vals[i] is not None:
            node.left = TreeNode(vals[i])
            q.append(node.left)
        i += 1
        if i < n and vals[i] is not None:
            node.right = TreeNode(vals[i])
            q.append(node.right)
        i += 1
    return root

def find_node(root: Optional[TreeNode], target: int) -> Optional[TreeNode]:
    """Finds a node by value with DFS (no BST assumptions to keep this brute-force)."""
    if not root:
        return None
    if root.val == target:
        return root
    left = find_node(root.left, target)
    if left:
        return left
    return find_node(root.right, target)

def path_to_node(root: Optional[TreeNode], target: int) -> List[TreeNode]:
    """Returns the path from root to target node (inclusive). Raises if not found."""
    path = []
    def dfs(node: Optional[TreeNode]) -> bool:
        if not node:
            return False
        path.append(node)
        if node.val == target:
            return True
        if dfs(node.left) or dfs(node.right):
            return True
        path.pop()
        return False
    found = dfs(root)
    if not found:
        raise ValueError(f"Node with value {target} not found in tree.")
    return path

def lowest_common_ancestor_bruteforce(root: TreeNode, p_val: int, q_val: int) -> TreeNode:
    p_path = path_to_node(root, p_val)
    q_path = path_to_node(root, q_val)
    lca = None
    for a, b in zip(p_path, q_path):
        if a is b:
            lca = a
        else:
            break
    return lca

# --- Demo / simple tests ---
if __name__ == "__main__":
    # Example 1
    root = build_tree_level([5,3,8,1,4,7,9,None,2])
    p, q = 3, 8
    print(lowest_common_ancestor_bruteforce(root, p, q).val)  # Expected 5

    # Example 2
    root = build_tree_level([5,3,8,1,4,7,9,None,2])
    p, q = 3, 4
    print(lowest_common_ancestor_bruteforce(root, p, q).val)  # Expected 3
