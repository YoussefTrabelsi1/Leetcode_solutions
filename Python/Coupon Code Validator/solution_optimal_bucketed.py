# filename: solution_optimal_bucketed.py
from typing import List

class Solution:
    def validCoupons(self, code: List[str], businessLine: List[str], isActive: List[bool]) -> List[str]:
        order = ["electronics", "grocery", "pharmacy", "restaurant"]
        rank = {bl: i for i, bl in enumerate(order)}

        def valid_code(s: str) -> bool:
            return bool(s) and all(ch.isalnum() or ch == "_" for ch in s)

        # 4 fixed buckets => linear categorization, then sort only within buckets
        buckets: List[List[str]] = [[] for _ in range(4)]
        for c, bl, active in zip(code, businessLine, isActive):
            if active and bl in rank and valid_code(c):
                buckets[rank[bl]].append(c)

        out: List[str] = []
        for b in buckets:
            b.sort()  # lexicographic
            out.extend(b)
        return out


if __name__ == "__main__":
    s = Solution()
    print(s.validCoupons(
        ["SAVE20", "", "PHARMA5", "SAVE@20"],
        ["restaurant", "grocery", "pharmacy", "restaurant"],
        [True, True, True, True]
    ))
    print(s.validCoupons(
        ["GROCERY15", "ELECTRONICS_50", "DISCOUNT10"],
        ["grocery", "electronics", "invalid"],
        [False, True, True]
    ))
