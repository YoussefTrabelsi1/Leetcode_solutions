# file: solution_optimal_spf.py

from typing import List
import math

class Solution:
    def _build_spf(self, n: int) -> List[int]:
        """Smallest Prime Factor sieve up to n."""
        spf = list(range(n + 1))
        if n >= 1:
            spf[1] = 1
        limit = int(math.isqrt(n))
        for i in range(2, limit + 1):
            if spf[i] == i:  # i is prime
                step = i
                start = i * i
                for j in range(start, n + 1, step):
                    if spf[j] == j:
                        spf[j] = i
        return spf

    def _four_div_sum(self, x: int, spf: List[int]) -> int:
        """
        Numbers with exactly 4 divisors are:
          1) x = p^3 (p prime) -> divisors: 1, p, p^2, p^3
          2) x = p*q (p, q distinct primes) -> divisors: 1, p, q, pq
        Return sum of divisors if exactly 4 divisors, else 0.
        """
        if x < 6:  # 1..5 can't have exactly 4 divisors
            return 0

        factors = {}
        tmp = x
        while tmp > 1:
            p = spf[tmp]
            c = 0
            while tmp % p == 0:
                tmp //= p
                c += 1
            factors[p] = factors.get(p, 0) + c

            # small pruning: more than 2 distinct primes or exponent too large can't be 4 divisors
            if len(factors) > 2:
                return 0

        if len(factors) == 1:
            (p, a), = factors.items()
            if a == 3:
                # 1 + p + p^2 + p^3
                return 1 + p + p * p + p * p * p
            return 0

        if len(factors) == 2:
            items = list(factors.items())
            (p, a), (q, b) = items[0], items[1]
            if a == 1 and b == 1:
                # (1+p)(1+q) = 1 + p + q + pq
                return (1 + p) * (1 + q)
            return 0

        return 0

    def sumFourDivisors(self, nums: List[int]) -> int:
        if not nums:
            return 0
        maxv = max(nums)
        spf = self._build_spf(maxv)

        total = 0
        for x in nums:
            total += self._four_div_sum(x, spf)
        return total


if __name__ == "__main__":
    sol = Solution()
    print(sol.sumFourDivisors([21, 4, 7]))      # 32
    print(sol.sumFourDivisors([21, 21]))        # 64
    print(sol.sumFourDivisors([1, 2, 3, 4, 5])) # 0
    print(sol.sumFourDivisors([8, 6, 10, 16]))  # 15 + 12 + 18 + 0 = 45
