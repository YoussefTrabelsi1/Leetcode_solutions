# filename: solution_space_optimized_bitset.py
from typing import List

def min_deletion_size(strs: List[str]) -> int:
    """
    Same greedy logic, but tracks "undecided adjacent pairs" using a bitset.
    Space is tiny (one integer).
    Time:  O(n*m)
    Space: O(1) extra (conceptually)
    """
    n = len(strs)
    if n <= 1:
        return 0
    m = len(strs[0])

    # bit i == 1 means pair (i, i+1) is still undecided (equal so far)
    undecided = (1 << (n - 1)) - 1
    deletions = 0

    for j in range(m):
        # Check if column j is "bad" for any undecided pair
        x = undecided
        bad = False
        i = 0
        while x:
            if x & 1:
                if strs[i][j] > strs[i + 1][j]:
                    bad = True
                    break
            x >>= 1
            i += 1

        if bad:
            deletions += 1
            continue

        # Safe to keep: clear bits where we become strictly increasing at this column
        x = undecided
        i = 0
        while x:
            if x & 1:
                if strs[i][j] < strs[i + 1][j]:
                    undecided &= ~(1 << i)
            x >>= 1
            i += 1

        if undecided == 0:
            break

    return deletions

if __name__ == "__main__":
    print(min_deletion_size(["ca", "bb", "ac"]))  # 1
    print(min_deletion_size(["xc", "yb", "za"]))  # 0
    print(min_deletion_size(["zyx", "wvu", "tsr"]))  # 3
