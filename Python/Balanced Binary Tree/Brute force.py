# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def isBalanced_bruteforce(root: TreeNode) -> bool:
    def height(node):
        if not node:
            return 0
        return 1 + max(height(node.left), height(node.right))

    if not root:
        return True
    return (abs(height(root.left) - height(root.right)) <= 1
            and isBalanced_bruteforce(root.left)
            and isBalanced_bruteforce(root.right))
