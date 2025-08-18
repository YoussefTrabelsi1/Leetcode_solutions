# Build Tree from preorder + inorder (brute force with slicing)
# Time: O(n^2) due to repeated linear searches & slicing; Space: O(n)

import sys
sys.setrecursionlimit(1_000_000)

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def buildTree(preorder, inorder):
    if not preorder or not inorder:
        return None
    root_val = preorder[0]
    root_idx_in_inorder = inorder.index(root_val)  # O(n)
    root = TreeNode(root_val)

    # Left subtree is next 'root_idx_in_inorder' nodes in preorder
    root.left  = buildTree(preorder[1:1+root_idx_in_inorder], inorder[:root_idx_in_inorder])
    root.right = buildTree(preorder[1+root_idx_in_inorder:], inorder[root_idx_in_inorder+1:])
    return root

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
