# filename: solution_time_optimized.py
from typing import List

class Solution:
    def validCoupons(self, code: List[str], businessLine: List[str], isActive: List[bool]) -> List[str]:
        rank = {"electronics": 0, "grocery": 1, "pharmacy": 2, "restaurant": 3}

        def valid_code(s: str) -> bool:
            return bool(s) and all(ch.isalnum() or ch == "_" for ch in s)

        filtered: List[tuple[int, str]] = []
        for c, bl, active in zip(code, businessLine, isActive):
            if active and bl in rank and valid_code(c):
                filtered.append((rank[bl], c))

        filtered.sort(key=lambda x: (x[0], x[1]))
        return [c for _, c in filtered]


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
