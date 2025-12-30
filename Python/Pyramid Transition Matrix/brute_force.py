# brute_force.py
# Brute force backtracking: generate every possible upper row (no memoization).

from typing import List, Dict


class Solution:
    def pyramidTransition(self, bottom: str, allowed: List[str]) -> bool:
        nxt: Dict[str, List[str]] = {}
        for t in allowed:
            pair = t[:2]
            nxt.setdefault(pair, []).append(t[2])

        def build(row: str) -> bool:
            if len(row) == 1:
                return True

            # Build all possible next rows (brute force)
            options = []

            def backtrack(i: int, cur: List[str]) -> None:
                if i == len(row) - 1:
                    options.append("".join(cur))
                    return
                pair = row[i : i + 2]
                if pair not in nxt:
                    return
                for ch in nxt[pair]:
                    cur.append(ch)
                    backtrack(i + 1, cur)
                    cur.pop()

            backtrack(0, [])

            for upper in options:
                if build(upper):
                    return True
            return False

        return build(bottom)


if __name__ == "__main__":
    s = Solution()
    print(s.pyramidTransition("BCD", ["BCC", "CDE", "CEA", "FFF"]))  # True
    print(s.pyramidTransition("AAAA", ["AAB", "AAC", "BCD", "BBE", "DEF"]))  # False
