# filename: brute_force_dfs_pruning.py

from typing import List

class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        n = len(strs)
        m = len(strs[0])

        # Track best number of kept columns found so far
        best_keep = 0

        # last[r] = last kept character code (0..25) in row r, or -1 if none kept yet
        last = [-1] * n

        def dfs(i: int, kept: int) -> None:
            nonlocal best_keep

            # Upper bound: even if we keep everything remaining
            if kept + (m - i) <= best_keep:
                return

            if i == m:
                best_keep = max(best_keep, kept)
                return

            # Option 1: delete column i
            dfs(i + 1, kept)

            # Option 2: keep column i if it doesn't break nondecreasing order in any row
            can_keep = True
            cur_chars = [0] * n
            for r in range(n):
                c = ord(strs[r][i]) - 97
                cur_chars[r] = c
                if c < last[r]:
                    can_keep = False
                    break

            if can_keep:
                old = last[:]  # brute-force: copy whole state
                for r in range(n):
                    last[r] = cur_chars[r]
                dfs(i + 1, kept + 1)
                last[:] = old

        dfs(0, 0)
        return m - best_keep


if __name__ == "__main__":
    sol = Solution()
    print(sol.minDeletionSize(["babca", "bbazb"]))  # 3
    print(sol.minDeletionSize(["edcba"]))           # 4
    print(sol.minDeletionSize(["ghi", "def", "abc"]))  # 0
