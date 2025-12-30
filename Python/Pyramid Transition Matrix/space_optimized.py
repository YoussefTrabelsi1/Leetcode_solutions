# space_optimized.py
# Space-lean DFS: no list of next rows; builds one upper row in-place and recurses immediately.

from typing import List, Dict


class Solution:
    def pyramidTransition(self, bottom: str, allowed: List[str]) -> bool:
        nxt: Dict[str, List[str]] = {}
        for t in allowed:
            pair = t[:2]
            nxt.setdefault(pair, []).append(t[2])

        def dfs(row: str) -> bool:
            n = len(row)
            if n == 1:
                return True

            upper = [""] * (n - 1)

            def fill(i: int) -> bool:
                if i == n - 1:
                    return dfs("".join(upper))
                pair = row[i : i + 2]
                tops = nxt.get(pair)
                if not tops:
                    return False
                for ch in tops:
                    upper[i] = ch
                    if fill(i + 1):
                        return True
                return False

            return fill(0)

        return dfs(bottom)


if __name__ == "__main__":
    s = Solution()
    print(s.pyramidTransition("BCD", ["BCC", "CDE", "CEA", "FFF"]))  # True
    print(s.pyramidTransition("AAAA", ["AAB", "AAC", "BCD", "BBE", "DEF"]))  # False
