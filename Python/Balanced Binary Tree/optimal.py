# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def isBalanced_optimal(root: TreeNode) -> bool:
    def dfs(node):
        if not node:
            return 0
        lh = dfs(node.left)
        if lh == -1:
            return -1
        rh = dfs(node.right)
        if rh == -1:
            return -1
        if abs(lh - rh) > 1:
            return -1
        return 1 + max(lh, rh)

    return dfs(root) != -1
