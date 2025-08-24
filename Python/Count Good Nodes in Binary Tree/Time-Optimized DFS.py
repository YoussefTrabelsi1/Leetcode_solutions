# Time-Optimal: Single DFS with "max_so_far" carried down.
# Complexity: O(n) time, O(h) recursion stack, where h is tree height.

from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val, self.left, self.right = val, left, right

def build_tree(level_list):
    if not level_list:
        return None
    arr = [None if (x is None or (isinstance(x, str) and x.lower() == "null")) else x for x in level_list]
    root = TreeNode(arr[0])
    q = deque([root])
    i = 1
    while q and i < len(arr):
        node = q.popleft()
        if node:
            if i < len(arr):
                if arr[i] is not None:
                    node.left = TreeNode(arr[i]); q.append(node.left)
                i += 1
            if i < len(arr):
                if arr[i] is not None:
                    node.right = TreeNode(arr[i]); q.append(node.right)
                i += 1
    return root

def count_good_nodes_dfs(root):
    def dfs(node, max_so_far):
        if not node: return 0
        good = 1 if node.val >= max_so_far else 0
        new_max = max(max_so_far, node.val)
        return good + dfs(node.left, new_max) + dfs(node.right, new_max)
    if not root: return 0
    return dfs(root, root.val)

# ---- Tests ----
root1 = build_tree([2,1,1,3,'null',1,5])
root2 = build_tree([1,2,-1,3,4])
print(count_good_nodes_dfs(root1))  # expected 3
print(count_good_nodes_dfs(root2))  # expected 4
