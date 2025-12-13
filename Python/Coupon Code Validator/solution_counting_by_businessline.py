# filename: solution_counting_by_businessline.py
from typing import List

class Solution:
    def validCoupons(self, code: List[str], businessLine: List[str], isActive: List[bool]) -> List[str]:
        # Since there are only 4 business lines, we can "count" them into fixed bins
        # and then only do lex sort within each bin.
        order = ("electronics", "grocery", "pharmacy", "restaurant")

        def valid_code(s: str) -> bool:
            if not s:
                return False
            for ch in s:
                if not (ch.isalnum() or ch == "_"):
                    return False
            return True

        # fixed 4 bins, no dict needed
        b0: List[str] = []
        b1: List[str] = []
        b2: List[str] = []
        b3: List[str] = []

        for c, bl, active in zip(code, businessLine, isActive):
            if not active or not valid_code(c):
                continue

            if bl == order[0]:
                b0.append(c)
            elif bl == order[1]:
                b1.append(c)
            elif bl == order[2]:
                b2.append(c)
            elif bl == order[3]:
                b3.append(c)
            # else: invalid business line -> ignore

        b0.sort()
        b1.sort()
        b2.sort()
        b3.sort()
        return b0 + b1 + b2 + b3


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
