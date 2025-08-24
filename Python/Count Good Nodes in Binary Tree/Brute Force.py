# Brute Force: For every node, search the path from root to that node to get the path max.
# Complexity: O(n^2) time in the worst case (skewed tree), O(h) recursion stack.

from collections import deque
import math

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val, self.left, self.right = val, left, right

def build_tree(level_list):
    # Accepts Python None or string "null"
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

def gather_nodes(root):
    nodes = []
    def dfs(n):
        if not n: return
        nodes.append(n)
        dfs(n.left); dfs(n.right)
    dfs(root)
    return nodes

def path_max_from_root(root, target):
    """
    Returns (found, path_max) where path_max is the maximum value on the unique root->target path (including target).
    """
    if not root:
        return (False, -math.inf)
    if root is target:
        return (True, root.val)
    # search left
    found, m = path_max_from_root(root.left, target)
    if found:
        return (True, max(root.val, m))
    # search right
    found, m = path_max_from_root(root.right, target)
    if found:
        return (True, max(root.val, m))
    return (False, -math.inf)

def count_good_nodes_bruteforce(root):
    if not root: return 0
    nodes = gather_nodes(root)
    good = 0
    for node in nodes:
        found, pm = path_max_from_root(root, node)
        # Node is good iff its value equals the max on the entire path (i.e., it was never smaller than any ancestor).
        if found and pm == node.val:
            good += 1
    return good

# ---- Tests ----
root1 = build_tree([2,1,1,3,'null',1,5])
root2 = build_tree([1,2,-1,3,4])
print(count_good_nodes_bruteforce(root1))  # expected 3
print(count_good_nodes_bruteforce(root2))  # expected 4
