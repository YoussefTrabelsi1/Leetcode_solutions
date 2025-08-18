# Build Tree iteratively using a stack; avoids O(n) hashmap
# Time: O(n); Extra Space: O(h) where h is tree height (stack)

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def buildTree(preorder, inorder):
    if not preorder:
        return None
    root = TreeNode(preorder[0])
    stack = [root]
    in_idx = 0  # pointer in inorder

    for val in preorder[1:]:
        node = stack[-1]
        if node.val != inorder[in_idx]:
            # Next preorder value is left child
            node.left = TreeNode(val)
            stack.append(node.left)
        else:
            # Rewind up to find the parent for the right child
            while stack and stack[-1].val == inorder[in_idx]:
                node = stack.pop()
                in_idx += 1
            node.right = TreeNode(val)
            stack.append(node.right)
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
