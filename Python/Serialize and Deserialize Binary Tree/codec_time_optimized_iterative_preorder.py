# filename: codec_time_optimized_iterative_preorder.py

from typing import Optional, List
from collections import deque


class TreeNode:
    def __init__(self, val: int = 0,
                 left: Optional["TreeNode"] = None,
                 right: Optional["TreeNode"] = None):
        self.val = val
        self.left = left
        self.right = right


class CodecTimeOptimized:
    """
    Time-optimized: iterative preorder for serialize to reduce recursion overhead.
    Deserialize uses index over list (no iterator object).
    Overall still O(n) time/space but with low constant factors.
    """

    def serialize(self, root: Optional[TreeNode]) -> str:
        if not root:
            return ""
        res: List[str] = []
        stack = [root]
        while stack:
            node = stack.pop()
            if node:
                res.append(str(node.val))
                # push right first so left is processed first
                stack.append(node.right)
                stack.append(node.left)
            else:
                res.append("#")
        return ",".join(res)

    def deserialize(self, data: str) -> Optional[TreeNode]:
        if not data:
            return None
        vals = data.split(",")
        index = 0
        n = len(vals)

        def build() -> Optional[TreeNode]:
            nonlocal index
            if index >= n:
                return None
            v = vals[index]
            index += 1
            if v == "#":
                return None
            node = TreeNode(int(v))
            node.left = build()
            node.right = build()
            return node

        return build()


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
    codec = CodecTimeOptimized()

    root = TreeNode(1,
                    TreeNode(2),
                    TreeNode(3, TreeNode(4), TreeNode(5)))
    s = codec.serialize(root)
    restored = codec.deserialize(s)
    print(to_level_order_list(restored))  # [1, 2, 3, None, None, 4, 5]

    root2 = None
    s2 = codec.serialize(root2)
    restored2 = codec.deserialize(s2)
    print(to_level_order_list(restored2))  # []
