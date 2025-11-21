# filename: codec_space_optimized_bfs.py

from typing import Optional, List
from collections import deque


class TreeNode:
    def __init__(self, val: int = 0,
                 left: Optional["TreeNode"] = None,
                 right: Optional["TreeNode"] = None):
        self.val = val
        self.left = left
        self.right = right


class CodecSpaceOptimized:
    """
    Space-optimized: level-order + trimming trailing nulls.
    Same O(n) time, smaller serialized string on average.
    """

    def serialize(self, root: Optional[TreeNode]) -> str:
        if not root:
            return ""
        res: List[str] = []
        q = deque([root])
        while q:
            node = q.popleft()
            if node:
                res.append(str(node.val))
                q.append(node.left)
                q.append(node.right)
            else:
                res.append("#")

        # Remove trailing "#" to shrink the string
        while res and res[-1] == "#":
            res.pop()

        return ",".join(res)

    def deserialize(self, data: str) -> Optional[TreeNode]:
        if not data:
            return None
        vals = data.split(",")
        root = TreeNode(int(vals[0]))
        q = deque([root])
        i = 1

        while q and i < len(vals):
            node = q.popleft()

            # left child
            if i < len(vals):
                if vals[i] != "#":
                    node.left = TreeNode(int(vals[i]))
                    q.append(node.left)
                i += 1

            # right child
            if i < len(vals):
                if vals[i] != "#":
                    node.right = TreeNode(int(vals[i]))
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
    while res and res[-1] is None:
        res.pop()
    return res


if __name__ == "__main__":
    codec = CodecSpaceOptimized()

    # Example 1
    # We'll manually build tree quickly
    root = TreeNode(1,
                    TreeNode(2),
                    TreeNode(3, TreeNode(4), TreeNode(5)))
    s = codec.serialize(root)
    restored = codec.deserialize(s)
    print(to_level_order_list(restored))  # [1, 2, 3, None, None, 4, 5]

    # Example 2
    root2 = None
    s2 = codec.serialize(root2)
    restored2 = codec.deserialize(s2)
    print(to_level_order_list(restored2))  # []
