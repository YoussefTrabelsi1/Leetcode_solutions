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

def level_order_bfs(root: Optional[TreeNode]) -> List[List[int]]:
    if not root:
        return []
    ans = []
    q = deque([root])

    while q:
        level_size = len(q)
        level = []
        for _ in range(level_size):
            node = q.popleft()
            level.append(node.val)
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)
        ans.append(level)
    return ans

# Example
root = build_tree([1, 2, 3, 4, 5, 6, 7])
print(level_order_bfs(root))  # [[1],[2,3],[4,5,6,7]]
