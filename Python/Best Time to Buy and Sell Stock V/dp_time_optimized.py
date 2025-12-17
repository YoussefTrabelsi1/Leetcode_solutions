# dp_time_optimized.py
# Same O(n*k) but tighter inner loop (less copying), using preallocated arrays.

from typing import List

class Solution:
    def maxProfit(self, prices: List[int], k: int) -> int:
        NEG = -10**30

        flat = [NEG] * (k + 1)
        longp = [NEG] * (k + 1)
        shortp = [NEG] * (k + 1)
        flat[0] = 0

        nflat = [NEG] * (k + 1)
        nlong = [NEG] * (k + 1)
        nshort = [NEG] * (k + 1)

        for p in prices:
            # reset next arrays to current (do nothing)
            for c in range(k + 1):
                nflat[c] = flat[c]
                nlong[c] = longp[c]
                nshort[c] = shortp[c]

            for c in range(k + 1):
                f = flat[c]
                l = longp[c]
                s = shortp[c]

                # open from flat
                if f > NEG // 2:
                    v = f - p
                    if v > nlong[c]:
                        nlong[c] = v
                    v = f + p
                    if v > nshort[c]:
                        nshort[c] = v

                # close positions
                if c < k:
                    if l > NEG // 2:
                        v = l + p
                        if v > nflat[c + 1]:
                            nflat[c + 1] = v
                    if s > NEG // 2:
                        v = s - p
                        if v > nflat[c + 1]:
                            nflat[c + 1] = v

            flat, nflat = nflat, flat
            longp, nlong = nlong, longp
            shortp, nshort = nshort, shortp

        return max(flat)
