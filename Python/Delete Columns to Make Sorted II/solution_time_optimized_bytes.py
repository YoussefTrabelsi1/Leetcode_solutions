# filename: solution_time_optimized_bytes.py
from typing import List

def min_deletion_size(strs: List[str]) -> int:
    """
    Same optimal greedy, but uses bytes for faster indexing (ints) in tight loops.
    Often faster in Python on larger inputs.
    Time:  O(n*m)
    Space: O(n)
    """
    n = len(strs)
    if n <= 1:
        return 0
    m = len(strs[0])

    rows = [s.encode("ascii") for s in strs]  # bytes indexing returns int
    decided = bytearray(n - 1)  # 0/1 flags
    undecided_count = n - 1
    deletions = 0

    for j in range(m):
        # check bad
        bad = False
        for i in range(n - 1):
            if not decided[i] and rows[i][j] > rows[i + 1][j]:
                bad = True
                break
        if bad:
            deletions += 1
            continue

        # update decided
        for i in range(n - 1):
            if not decided[i] and rows[i][j] < rows[i + 1][j]:
                decided[i] = 1
                undecided_count -= 1

        if undecided_count == 0:
            break

    return deletions

if __name__ == "__main__":
    print(min_deletion_size(["ca", "bb", "ac"]))  # 1
    print(min_deletion_size(["xc", "yb", "za"]))  # 0
    print(min_deletion_size(["zyx", "wvu", "tsr"]))  # 3
