# time_optimized.py
# Fast version: bitmask transitions + memoization on row strings (aggressive pruning).

from typing import List
from functools import lru_cache


class Solution:
    def pyramidTransition(self, bottom: str, allowed: List[str]) -> bool:
        # Map A-F -> 0..5
        def idx(c: str) -> int:
            return ord(c) - ord("A")

        # pair_mask[a][b] is a 6-bit mask of possible tops over (a,b)
        pair_mask = [[0] * 6 for _ in range(6)]
        for t in allowed:
            a, b, c = idx(t[0]), idx(t[1]), idx(t[2])
            pair_mask[a][b] |= 1 << c

        @lru_cache(None)
        def can(row: str) -> bool:
            if len(row) == 1:
                return True

            n = len(row)
            upper = [0] * (n - 1)  # store indices 0..5 while building

            # quick dead-end check (any adjacent pair has no possible top)
            for i in range(n - 1):
                if pair_mask[idx(row[i])][idx(row[i + 1])] == 0:
                    return False

            def fill(i: int) -> bool:
                if i == n - 1:
                    upper_str = "".join(chr(u + ord("A")) for u in upper)
                    return can(upper_str)

                m = pair_mask[idx(row[i])][idx(row[i + 1])]
                while m:
                    lsb = m & -m
                    top = (lsb.bit_length() - 1)
                    upper[i] = top
                    if fill(i + 1):
                        return True
                    m -= lsb
                return False

            return fill(0)

        return can(bottom)


if __name__ == "__main__":
    s = Solution()
    print(s.pyramidTransition("BCD", ["BCC", "CDE", "CEA", "FFF"]))  # True
    print(s.pyramidTransition("AAAA", ["AAB", "AAC", "BCD", "BBE", "DEF"]))  # False
