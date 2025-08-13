# Brute force: build each level's values, then keep the last one (rightmost).
# Time: O(n). Space: O(w), where w is the max width of the tree.

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
    # Treat 'null' string as None as well.
    def isnull(x): return x is None or x == "null"
    root = TreeNode(arr[0])
    q = deque([root])
    i = 1
    while q and i < len(arr):
        node = q.popleft()
        if i < len(arr) and not isnull(arr[i]):
            node.left = TreeNode(arr[i])
            q.append(node.left)
        i += 1
        if i < len(arr) and not isnull(arr[i]):
            node.right = TreeNode(arr[i])
            q.append(node.right)
        i += 1
    return root

def right_side_view_bruteforce(root: Optional[TreeNode]) -> List[int]:
    if not root:
        return []
    q = deque([root])
    ans = []
    while q:
        level_vals = []
        for _ in range(len(q)):
            node = q.popleft()
            level_vals.append(node.val)
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)
        ans.append(level_vals[-1])  # rightmost at this level
    return ans

# --- Demo ---
if __name__ == "__main__":
    print(right_side_view_bruteforce(list_to_tree([1,2,3])))               # [1, 3]
    print(right_side_view_bruteforce(list_to_tree([1,2,3,4,5,6,7])))       # [1, 3, 7]
