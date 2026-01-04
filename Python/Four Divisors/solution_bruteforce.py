# file: solution_bruteforce.py

from typing import List

class Solution:
    def sumFourDivisors(self, nums: List[int]) -> int:
        total = 0

        for x in nums:
            cnt = 0
            s = 0
            d = 1
            while d <= x:
                if x % d == 0:
                    cnt += 1
                    s += d
                    if cnt > 4:   # early stop
                        break
                d += 1

            if cnt == 4:
                total += s

        return total


if __name__ == "__main__":
    sol = Solution()
    print(sol.sumFourDivisors([21, 4, 7]))      # 32
    print(sol.sumFourDivisors([21, 21]))        # 64
    print(sol.sumFourDivisors([1, 2, 3, 4, 5])) # 0
