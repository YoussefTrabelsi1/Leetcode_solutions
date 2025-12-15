# file: solution4_two_pointers_segments.py
# Two-pointers: split into maximal descent-by-1 segments, sum L*(L+1)//2
# O(n) time, O(1) space

from typing import List

class Solution:
    def getDescentPeriods(self, prices: List[int]) -> int:
        n = len(prices)
        ans = 0
        i = 0

        while i < n:
            j = i
            while j + 1 < n and prices[j] - prices[j + 1] == 1:
                j += 1
            L = j - i + 1
            ans += L * (L + 1) // 2
            i = j + 1

        return ans

if __name__ == "__main__":
    s = Solution()
    print(s.getDescentPeriods([3, 2, 1, 4]))  # 7
    print(s.getDescentPeriods([8, 6, 7, 7]))  # 4
    print(s.getDescentPeriods([1]))           # 1
