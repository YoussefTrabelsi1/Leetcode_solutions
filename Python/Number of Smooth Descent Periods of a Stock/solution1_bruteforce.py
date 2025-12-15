# file: solution1_bruteforce.py
# Brute force O(n^2) worst-case

from typing import List

class Solution:
    def getDescentPeriods(self, prices: List[int]) -> int:
        n = len(prices)
        ans = 0
        for i in range(n):
            ans += 1  # single day always valid
            for j in range(i + 1, n):
                if prices[j - 1] - prices[j] == 1:
                    ans += 1
                else:
                    break
        return ans

if __name__ == "__main__":
    s = Solution()
    print(s.getDescentPeriods([3, 2, 1, 4]))  # 7
    print(s.getDescentPeriods([8, 6, 7, 7]))  # 4
    print(s.getDescentPeriods([1]))           # 1
