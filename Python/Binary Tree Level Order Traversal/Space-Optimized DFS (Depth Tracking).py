from collections import deque
from typing import Optional, List

class TreeNode:
    def __init__(self, val: int = 0, left: 'TreeNode' = None, right: 'TreeNode' = None):
        self.val = val
        self.left = left
        self.right = right

def build_tree(level_list: List[Optional[int]]) -> Optional[TreeNode]:
    if not level_list:
        return None
    it = iter(level_list)
    first = next(it)
    if first is None:
        return None
    root = TreeNode(first)
    q = deque([root])

    for val in it:
        if not q:
            break
        node = q.popleft()
        if val is not None:
            node.left = TreeNode(val)
            q.append(node.left)
        try:
            right_val = next(it)
        except StopIteration:
            break
        if right_val is not None:
            node.right = TreeNode(right_val)
            q.append(node.right)
    return root

def level_order_dfs(root: Optional[TreeNode]) -> List[List[int]]:
    ans = []
    def dfs(node: Optional[TreeNode], depth: int):
        if not node:
            return
        if depth == len(ans):
            ans.append([])
        ans[depth].append(node.val)
        dfs(node.left, depth + 1)
        dfs(node.right, depth + 1)
    dfs(root, 0)
    return ans

# Example
root = build_tree([1, 2, 3, 4, 5, 6, 7])
print(level_order_dfs(root))  # [[1],[2,3],[4,5,6,7]]
