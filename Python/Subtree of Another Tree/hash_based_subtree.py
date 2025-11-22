# file: hash_based_subtree.py

from collections import deque
from typing import Optional, List, Tuple, Dict


class TreeNode:
    def __init__(self, val: int = 0,
                 left: Optional["TreeNode"] = None,
                 right: Optional["TreeNode"] = None):
        self.val = val
        self.left = left
        self.right = right


def build_tree(level: List[Optional[int]]) -> Optional[TreeNode]:
    if not level:
        return None
    it = iter(level)
    root = TreeNode(next(it))
    q = deque([root])

    for v in it:
        node = q.popleft()
        if v is not None:
            node.left = TreeNode(v)
            q.append(node.left)
        try:
            v = next(it)
        except StopIteration:
            break
        if v is not None:
            node.right = TreeNode(v)
            q.append(node.right)
    return root


def compute_hashes(root: Optional[TreeNode]) -> Tuple[Dict[TreeNode, Tuple[int, int]], Optional[TreeNode]]:
    """
    Compute a structural hash for every subtree.
    Returns:
        hashes: map node -> (hash_value, size_of_subtree)
        root: same root pointer back
    Hash is based on (val, left_hash, right_hash, size).
    """
    hashes: Dict[TreeNode, Tuple[int, int]] = {}
    MOD = 10**9 + 7
    BASE = 129

    def dfs(node: Optional[TreeNode]) -> Tuple[int, int]:
        if not node:
            return (3, 0)  # arbitrary non-zero hash for null, size 0
        lh, ls = dfs(node.left)
        rh, rs = dfs(node.right)
        size = ls + rs + 1
        # Combine into a hash value
        h = (node.val * BASE * BASE * BASE +
             lh * BASE * BASE +
             rh * BASE +
             size) % MOD
        hashes[node] = (h, size)
        return h, size

    dfs(root)
    return hashes, root


def is_subtree(root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
    """
    Hash-based subtree check (like Merkle trees).
    Time: O(N + M) expected
    Space: O(N + M)
    """
    if subRoot is None:
        return True
    if root is None:
        return False

    sub_hashes, _ = compute_hashes(subRoot)
    root_hashes, _ = compute_hashes(root)

    # Hash of entire subRoot
    # subRoot is the root passed, so its hash is in the dict.
    sub_root_hash = sub_hashes[subRoot]

    # Now see if any node in root has the same (hash, size)
    for h_size in root_hashes.values():
        if h_size == sub_root_hash:
            return True
    return False


if __name__ == "__main__":
    root = build_tree([1, 2, 3, 4, 5])
    sub = build_tree([2, 4, 5])
    print(is_subtree(root, sub))  # True

    root2 = build_tree([1, 2, 3, 4, 5, None, None, 6])
    sub2 = build_tree([2, 4, 5])
    print(is_subtree(root2, sub2))  # False
