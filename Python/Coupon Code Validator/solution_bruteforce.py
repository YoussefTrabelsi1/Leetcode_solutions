# filename: solution_bruteforce.py
from typing import List

class Solution:
    def validCoupons(self, code: List[str], businessLine: List[str], isActive: List[bool]) -> List[str]:
        order = ["electronics", "grocery", "pharmacy", "restaurant"]
        allowed = set(order)

        def valid_code(s: str) -> bool:
            if not s:
                return False
            for ch in s:
                if not (ch.isalnum() or ch == "_"):
                    return False
            return True

        def bubble_sort(arr: List[str]) -> None:
            # O(k^2) brute sort
            k = len(arr)
            for i in range(k):
                for j in range(0, k - 1 - i):
                    if arr[j] > arr[j + 1]:
                        arr[j], arr[j + 1] = arr[j + 1], arr[j]

        n = len(code)
        ans: List[str] = []

        # Brute: scan all coupons for each category, then bubble sort inside it
        for bl in order:
            bucket: List[str] = []
            for i in range(n):
                if isActive[i] and businessLine[i] == bl and businessLine[i] in allowed and valid_code(code[i]):
                    bucket.append(code[i])
            bubble_sort(bucket)
            ans.extend(bucket)

        return ans


if __name__ == "__main__":
    s = Solution()
    print(s.validCoupons(
        ["SAVE20", "", "PHARMA5", "SAVE@20"],
        ["restaurant", "grocery", "pharmacy", "restaurant"],
        [True, True, True, True]
    ))  # ["PHARMA5","SAVE20"]

    print(s.validCoupons(
        ["GROCERY15", "ELECTRONICS_50", "DISCOUNT10"],
        ["grocery", "electronics", "invalid"],
        [False, True, True]
    ))  # ["ELECTRONICS_50"]
