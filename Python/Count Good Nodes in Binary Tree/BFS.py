# BFS level-order traversal while carrying "max_so_far".
# Complexity: O(n) time, O(w) space, where w is the tree's max width.

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

def count_good_nodes_bfs(root):
    if not root: return 0
    q = deque([(root, root.val)])
    good = 0
    while q:
        node, max_so_far = q.popleft()
        if node.val >= max_so_far:
            good += 1
        new_max = max(max_so_far, node.val)
        if node.left:
            q.append((node.left, new_max))
        if node.right:
            q.append((node.right, new_max))
    return good

# ---- Tests ----
root1 = build_tree([2,1,1,3,'null',1,5])
root2 = build_tree([1,2,-1,3,4])
print(count_good_nodes_bfs(root1))  # expected 3
print(count_good_nodes_bfs(root2))  # expected 4
