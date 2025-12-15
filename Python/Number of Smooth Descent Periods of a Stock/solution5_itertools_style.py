# file: solution5_itertools_style.py
# Same optimal idea, written in a compact "streaming" style
# O(n) time, O(1) space

from typing import List

class Solution:
    def getDescentPeriods(self, prices: List[int]) -> int:
        if not prices:
            return 0

        ans = 1
        run = 1
        for prev, cur in zip(prices, prices[1:]):
            if prev - cur == 1:
                run += 1
            else:
                run = 1
            ans += run
        return ans

if __name__ == "__main__":
    s = Solution()
    print(s.getDescentPeriods([3, 2, 1, 4]))  # 7
    print(s.getDescentPeriods([8, 6, 7, 7]))  # 4
    print(s.getDescentPeriods([1]))           # 1
