# file: solution_sqrt_stream.py

from typing import List
import math

class Solution:
    def sumFourDivisors(self, nums: List[int]) -> int:
        total = 0

        for x in nums:
            cnt = 0
            s = 0
            r = int(math.isqrt(x))

            for d in range(1, r + 1):
                if x % d != 0:
                    continue

                q = x // d
                if d == q:
                    cnt += 1
                    s += d
                else:
                    cnt += 2
                    s += d + q

                if cnt > 4:  # early stop
                    break

            if cnt == 4:
                total += s

        return total


if __name__ == "__main__":
    sol = Solution()
    print(sol.sumFourDivisors([21, 4, 7]))      # 32
    print(sol.sumFourDivisors([21, 21]))        # 64
    print(sol.sumFourDivisors([1, 2, 3, 4, 5])) # 0
