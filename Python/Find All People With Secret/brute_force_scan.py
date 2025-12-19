# filename: brute_force_scan.py
from typing import List, Dict, Tuple
from collections import defaultdict

class Solution:
    def findAllPeople(self, n: int, meetings: List[List[int]], firstPerson: int) -> List[int]:
        # Brute force idea:
        # For each time group, repeatedly scan meetings until no new person learns the secret.
        # This is correct but can be slow (worst-case quadratic per time group).

        know = [False] * n
        know[0] = True
        know[firstPerson] = True

        by_time: Dict[int, List[Tuple[int, int]]] = defaultdict(list)
        for x, y, t in meetings:
            by_time[t].append((x, y))

        for t in sorted(by_time.keys()):
            edges = by_time[t]
            changed = True
            while changed:
                changed = False
                for x, y in edges:
                    if know[x] or know[y]:
                        if not know[x]:
                            know[x] = True
                            changed = True
                        if not know[y]:
                            know[y] = True
                            changed = True

        return [i for i, v in enumerate(know) if v]


if __name__ == "__main__":
    sol = Solution()
    print(sol.findAllPeople(6, [[1,2,5],[2,3,8],[1,5,10]], 1))  # [0,1,2,3,5]
    print(sol.findAllPeople(4, [[3,1,3],[1,2,2],[0,3,3]], 3))   # [0,1,3]
    print(sol.findAllPeople(5, [[3,4,2],[1,2,1],[2,3,1]], 1))   # [0,1,2,3,4]
