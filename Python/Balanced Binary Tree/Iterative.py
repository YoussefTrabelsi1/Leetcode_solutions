class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def isBalanced_iterative(root: TreeNode) -> bool:
    if not root:
        return True
    stack = [(root, False)]
    height = {}
    while stack:
        node, seen = stack.pop()
        if not node:
            continue
        if not seen:
            stack.append((node, True))
            stack.append((node.right, False))
            stack.append((node.left, False))
        else:
            lh = height.get(node.left, 0)
            rh = height.get(node.right, 0)
            if abs(lh - rh) > 1:
                return False
            height[node] = 1 + max(lh, rh)
    return True
