# Time-lean BFS: push right child first; the first node popped at each level is the visible one.
# Avoids building level arrays; minimal per-level work.
# Time: O(n). Space: O(w).

from collections import deque
from typing import List, Optional, Union

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

def right_side_view_bfs_right_first(root: Optional[TreeNode]) -> List[int]:
    if not root:
        return []
    ans: List[int] = []
    q = deque([root])
    while q:
        level_size = len(q)
        for i in range(level_size):
            node = q.popleft()
            if i == 0:                 # first seen at this depth is the rightmost (since right enqueued first)
                ans.append(node.val)
            if node.right:
                q.append(node.right)
            if node.left:
                q.append(node.left)
    return ans

# --- Demo ---
if __name__ == "__main__":
    print(right_side_view_bfs_right_first(list_to_tree([1,2,3])))               # [1, 3]
    print(right_side_view_bfs_right_first(list_to_tree([1,2,3,4,5,6,7])))       # [1, 3, 7]
