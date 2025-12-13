# filename: solution_regex_validation.py
from typing import List
import re

class Solution:
    def validCoupons(self, code: List[str], businessLine: List[str], isActive: List[bool]) -> List[str]:
        order = ["electronics", "grocery", "pharmacy", "restaurant"]
        rank = {bl: i for i, bl in enumerate(order)}

        # fullmatch => whole string must be [A-Za-z0-9_]+ and non-empty
        pat = re.compile(r"^[A-Za-z0-9_]+$")

        valid_pairs: List[tuple[int, str]] = []
        for c, bl, active in zip(code, businessLine, isActive):
            if active and bl in rank and pat.fullmatch(c):
                valid_pairs.append((rank[bl], c))

        valid_pairs.sort()
        return [c for _, c in valid_pairs]


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
