# Build Tree using hashmap for inorder indices + pointer over preorder
# Time: O(n); Extra Space: O(n) for the hashmap + recursion stack

import sys
sys.setrecursionlimit(1_000_000)

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def buildTree(preorder, inorder):
    idx_map = {v: i for i, v in enumerate(inorder)}  # value -> inorder index
    pre_idx = 0

    def helper(in_left, in_right):
        nonlocal pre_idx
        if in_left > in_right:
            return None
        root_val = preorder[pre_idx]
        pre_idx += 1
        root = TreeNode(root_val)
        mid = idx_map[root_val]
        root.left  = helper(in_left, mid - 1)
        root.right = helper(mid + 1, in_right)
        return root

    return helper(0, len(inorder) - 1)

# Helpers for quick verification
from collections import deque
def serialize_level_order(root):
    if not root: return []
    res, q = [], deque([root])
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
    print(serialize_level_order(buildTree([1,2,3,4], [2,1,3,4])))  # [1, 2, 3, None, None, None, 4]
    print(serialize_level_order(buildTree([1], [1])))              # [1]
