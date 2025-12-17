# dp_space_optimized.py
# Rolling arrays: O(n*k) time, O(k) space.

from typing import List

class Solution:
    def maxProfit(self, prices: List[int], k: int) -> int:
        NEG = -10**30

        flat = [NEG] * (k + 1)
        longp = [NEG] * (k + 1)
        shortp = [NEG] * (k + 1)
        flat[0] = 0

        for p in prices:
            nflat = flat[:]    # "do nothing" baseline
            nlong = longp[:]
            nshort = shortp[:]

            for c in range(k + 1):
                # open from flat
                if flat[c] > NEG // 2:
                    if flat[c] - p > nlong[c]:
                        nlong[c] = flat[c] - p
                    if flat[c] + p > nshort[c]:
                        nshort[c] = flat[c] + p

                # close to flat (complete transaction)
                if c < k:
                    if longp[c] > NEG // 2:
                        val = longp[c] + p
                        if val > nflat[c + 1]:
                            nflat[c + 1] = val
                    if shortp[c] > NEG // 2:
                        val = shortp[c] - p
                        if val > nflat[c + 1]:
                            nflat[c + 1] = val

            flat, longp, shortp = nflat, nlong, nshort

        return max(flat)
