# filename: dp_time_optimized_bitsets.py

from typing import List

class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        n = len(strs)
        m = len(strs[0])
        if m == 0:
            return 0

        all_mask = (1 << m) - 1

        # For each row r:
        # pos_bits[r][c] = bitset of positions where character == c
        # ge_bits[r][c]  = bitset of positions where character >= c
        ge_bits = []
        for r in range(n):
            pos = [0] * 26
            s = strs[r]
            for i, ch in enumerate(s):
                pos[ord(ch) - 97] |= (1 << i)

            ge = [0] * 26
            running = 0
            for c in range(25, -1, -1):
                running |= pos[c]
                ge[c] = running
            ge_bits.append(ge)

        # valid_next[i] = bitset of j>i such that for all rows: strs[row][i] <= strs[row][j]
        valid_next = [0] * m
        for i in range(m):
            gt_mask = all_mask ^ ((1 << (i + 1)) - 1)  # bits for positions > i
            mask = gt_mask
            for r in range(n):
                c = ord(strs[r][i]) - 97
                mask &= ge_bits[r][c]
                if mask == 0:
                    break
            valid_next[i] = mask

        # DP over edges: dp[j] = longest chain ending at j
        dp = [1] * m
        best = 1

        for i in range(m):
            mask = valid_next[i]
            while mask:
                lsb = mask & -mask
                j = lsb.bit_length() - 1
                cand = dp[i] + 1
                if cand > dp[j]:
                    dp[j] = cand
                    if cand > best:
                        best = cand
                mask ^= lsb

        return m - best


if __name__ == "__main__":
    sol = Solution()
    print(sol.minDeletionSize(["babca", "bbazb"]))  # 3
    print(sol.minDeletionSize(["edcba"]))           # 4
    print(sol.minDeletionSize(["ghi", "def", "abc"]))  # 0
