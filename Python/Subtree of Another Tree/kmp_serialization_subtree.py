# file: kmp_serialization_subtree.py

from collections import deque
from typing import Optional, List


class TreeNode:
    def __init__(self, val: int = 0,
                 left: Optional["TreeNode"] = None,
                 right: Optional["TreeNode"] = None):
        self.val = val
        self.left = left
        self.right = right


def build_tree(level: List[Optional[int]]) -> Optional[TreeNode]:
    if not level:
        return None
    it = iter(level)
    root = TreeNode(next(it))
    q = deque([root])

    for v in it:
        node = q.popleft()
        if v is not None:
            node.left = TreeNode(v)
            q.append(node.left)
        try:
            v = next(it)
        except StopIteration:
            break
        if v is not None:
            node.right = TreeNode(v)
            q.append(node.right)
    return root


def serialize(root: Optional[TreeNode]) -> str:
    """
    Preorder with null markers so structure is preserved.
    Convert to string to apply substring search.
    """
    res = []

    def dfs(node: Optional[TreeNode]):
        if not node:
            res.append("#")  # null marker
            return
        res.append(f"{node.val}")
        dfs(node.left)
        dfs(node.right)

    dfs(root)
    # Add separator to avoid ambiguity e.g. "1#2" vs "11#2"
    return ",".join(res)


def build_lps(pattern: List[str]) -> List[int]:
    """
    Build LPS (longest prefix suffix) array for KMP.
    """
    lps = [0] * len(pattern)
    j = 0  # length of previous longest prefix suffix

    for i in range(1, len(pattern)):
        while j > 0 and pattern[i] != pattern[j]:
            j = lps[j - 1]
        if pattern[i] == pattern[j]:
            j += 1
            lps[i] = j
    return lps


def kmp_search(text: List[str], pattern: List[str]) -> bool:
    """
    KMP pattern search on list of tokens.
    """
    if not pattern:
        return True
    if not text:
        return False

    lps = build_lps(pattern)
    j = 0  # index for pattern

    for i in range(len(text)):
        while j > 0 and text[i] != pattern[j]:
            j = lps[j - 1]
        if text[i] == pattern[j]:
            j += 1
            if j == len(pattern):
                return True
    return False


def is_subtree(root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
    """
    Time-optimized (practically): serialize trees + KMP substring search.
    Time: O(N + M)
    Space: O(N + M)
    """
    # Empty subRoot: always subtree
    if subRoot is None:
        return True

    s_root = serialize(root)
    s_sub = serialize(subRoot)

    # Work token-wise to be precise
    text = s_root.split(",") if s_root else []
    pattern = s_sub.split(",") if s_sub else []

    return kmp_search(text, pattern)


if __name__ == "__main__":
    root = build_tree([1, 2, 3, 4, 5])
    sub = build_tree([2, 4, 5])
    print(is_subtree(root, sub))  # True

    root2 = build_tree([1, 2, 3, 4, 5, None, None, 6])
    sub2 = build_tree([2, 4, 5])
    print(is_subtree(root2, sub2))  # False
