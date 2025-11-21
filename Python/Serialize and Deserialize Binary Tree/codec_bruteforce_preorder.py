# filename: codec_bruteforce_preorder.py

from typing import Optional, List
from collections import deque


class TreeNode:
    def __init__(self, val: int = 0,
                 left: Optional["TreeNode"] = None,
                 right: Optional["TreeNode"] = None):
        self.val = val
        self.left = left
        self.right = right


class CodecBruteForce:
    """
    Brute force: recursive preorder + explicit null markers.
    Time: O(n), Space: O(n) for string + recursion.
    """

    def serialize(self, root: Optional[TreeNode]) -> str:
        vals: List[str] = []

        def dfs(node: Optional[TreeNode]) -> None:
            if not node:
                vals.append("#")
                return
            vals.append(str(node.val))
            dfs(node.left)
            dfs(node.right)

        dfs(root)
        return ",".join(vals)

    def deserialize(self, data: str) -> Optional[TreeNode]:
        if not data:
            return None

        vals = iter(data.split(","))

        def dfs() -> Optional[TreeNode]:
            v = next(vals)
            if v == "#":
                return None
            node = TreeNode(int(v))
            node.left = dfs()
            node.right = dfs()
            return node

        return dfs()


# Helpers for testing with level-order list format like [1,2,3,None,None,4,5]
def build_tree_level_order(arr: List[Optional[int]]) -> Optional[TreeNode]:
    if not arr:
        return None
    root = TreeNode(arr[0])
    q = deque([root])
    i = 1
    while q and i < len(arr):
        node = q.popleft()
        if i < len(arr) and arr[i] is not None:
            node.left = TreeNode(arr[i])
            q.append(node.left)
        i += 1
        if i < len(arr) and arr[i] is not None:
            node.right = TreeNode(arr[i])
            q.append(node.right)
        i += 1
    return root


def to_level_order_list(root: Optional[TreeNode]) -> List[Optional[int]]:
    if not root:
        return []
    res: List[Optional[int]] = []
    q = deque([root])
    while q:
        node = q.popleft()
        if node:
            res.append(node.val)
            q.append(node.left)
            q.append(node.right)
        else:
            res.append(None)
    # trim trailing None
    while res and res[-1] is None:
        res.pop()
    return res


if __name__ == "__main__":
    # Example 1
    root = build_tree_level_order([1, 2, 3, None, None, 4, 5])
    codec = CodecBruteForce()
    s = codec.serialize(root)
    restored = codec.deserialize(s)
    print(to_level_order_list(restored))  # [1, 2, 3, None, None, 4, 5]

    # Example 2 (empty tree)
    root2 = build_tree_level_order([])
    s2 = codec.serialize(root2)
    restored2 = codec.deserialize(s2)
    print(to_level_order_list(restored2))  # []
