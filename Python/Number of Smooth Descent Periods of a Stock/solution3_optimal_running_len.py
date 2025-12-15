# file: solution3_optimal_running_len.py
# Optimal O(n) time, O(1) space (running length)

from typing import List

class Solution:
    def getDescentPeriods(self, prices: List[int]) -> int:
        ans = 0
        run = 0  # length of current valid descent run ending at i

        for i in range(len(prices)):
            if i > 0 and prices[i - 1] - prices[i] == 1:
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
