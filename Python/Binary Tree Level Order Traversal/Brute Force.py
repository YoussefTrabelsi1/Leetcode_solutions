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

def level_order_bruteforce(root: Optional[TreeNode]) -> List[List[int]]:
    def height(node: Optional[TreeNode]) -> int:
        if not node:
            return 0
        return 1 + max(height(node.left), height(node.right))

    def collect_at_depth(node: Optional[TreeNode], depth: int, bag: List[int]):
        if not node:
            return
        if depth == 0:
            bag.append(node.val)
        else:
            collect_at_depth(node.left, depth - 1, bag)
            collect_at_depth(node.right, depth - 1, bag)

    if not root:
        return []
    h = height(root)
    ans = []
    for d in range(h):
        level_vals = []
        collect_at_depth(root, d, level_vals)
        ans.append(level_vals)
    return ans

# Example
root = build_tree([1, 2, 3, 4, 5, 6, 7])
print(level_order_bruteforce(root))  # [[1],[2,3],[4,5,6,7]]
