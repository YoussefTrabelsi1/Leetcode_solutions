# filename: solution_space_optimized.py
from typing import List

class Solution:
    def validCoupons(self, code: List[str], businessLine: List[str], isActive: List[bool]) -> List[str]:
        rank = {"electronics": 0, "grocery": 1, "pharmacy": 2, "restaurant": 3}

        def valid_code(s: str) -> bool:
            if not s:
                return False
            # avoids regex allocation; checks chars directly
            for ch in s:
                if not (ch.isalnum() or ch == "_"):
                    return False
            return True

        # Minimal extra storage: store only indices of valid coupons (besides the output itself)
        idx: List[int] = []
        for i in range(len(code)):
            bl = businessLine[i]
            if isActive[i] and bl in rank and valid_code(code[i]):
                idx.append(i)

        idx.sort(key=lambda i: (rank[businessLine[i]], code[i]))
        return [code[i] for i in idx]


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
