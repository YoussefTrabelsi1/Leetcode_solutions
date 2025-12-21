# filename: solution_greedy_optimal.py
from typing import List

def min_deletion_size(strs: List[str]) -> int:
    """
    Optimal greedy: scan columns left->right.
    Keep a column if it doesn't violate any still-tied adjacent pair.
    Otherwise delete it.
    Time:  O(n*m)
    Space: O(n)
    """
    n = len(strs)
    if n <= 1:
        return 0
    m = len(strs[0])

    # decided[i] means row i is already strictly smaller than row i+1 considering kept columns so far
    decided = [False] * (n - 1)
    deletions = 0

    for j in range(m):
        # Check if keeping this column would break lex order for any undecided adjacent pair
        for i in range(n - 1):
            if not decided[i] and strs[i][j] > strs[i + 1][j]:
                deletions += 1
                break
        else:
            # Safe to keep: now update which pairs become decided at this column
            for i in range(n - 1):
                if not decided[i] and strs[i][j] < strs[i + 1][j]:
                    decided[i] = True

            if all(decided):
                break

    return deletions

if __name__ == "__main__":
    print(min_deletion_size(["ca", "bb", "ac"]))  # 1
    print(min_deletion_size(["xc", "yb", "za"]))  # 0
    print(min_deletion_size(["zyx", "wvu", "tsr"]))  # 3
