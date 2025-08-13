# Space-optimized: DFS visiting right child first; record the first node seen at each depth.
# Time: O(n). Extra space: O(h) recursion stack (h = height), typically less than BFS width.

from typing import List, Optional, Union
from collections import deque

class TreeNode:
    def __init__(self, val: int = 0, left: 'Optional[TreeNode]' = None, right: 'Optional[TreeNode]' = None):
        self.val = val
        self.left = left
        self.right = right

def list_to_tree(arr: List[Union[int, None, str]]) -> Optional[TreeNode]:
    if not arr:
        return None
    def isnull(x): return x is None or x == "null"
    root = TreeNode(arr[0])
    q = deque([root])
    i = 1
    while q and i < len(arr):
        node = q.popleft()
        if i < len(arr) and not isnull(arr[i]):
            node.left = TreeNode(arr[i]); q.append(node.left)
        i += 1
        if i < len(arr) and not isnull(arr[i]):
            node.right = TreeNode(arr[i]); q.append(node.right)
        i += 1
    return root

def right_side_view_dfs(root: Optional[TreeNode]) -> List[int]:
    ans: List[int] = []
    def dfs(node: Optional[TreeNode], depth: int) -> None:
        if not node:
            return
        # First time we reach this depth (going right-first), this is the rightmost node.
        if depth == len(ans):
            ans.append(node.val)
        dfs(node.right, depth + 1)
        dfs(node.left, depth + 1)
    dfs(root, 0)
    return ans

# --- Demo ---
if __name__ == "__main__":
    print(right_side_view_dfs(list_to_tree([1,2,3])))               # [1, 3]
    print(right_side_view_dfs(list_to_tree([1,2,3,4,5,6,7])))       # [1, 3, 7]
