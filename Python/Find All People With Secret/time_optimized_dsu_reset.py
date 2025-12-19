# filename: time_optimized_dsu_reset.py
from typing import List

class DSU:
    __slots__ = ("parent", "size")

    def __init__(self, n: int):
        self.parent = list(range(n))
        self.size = [1] * n

    def find(self, x: int) -> int:
        while self.parent[x] != x:
            self.parent[x] = self.parent[self.parent[x]]
            x = self.parent[x]
        return x

    def union(self, a: int, b: int) -> None:
        ra, rb = self.find(a), self.find(b)
        if ra == rb:
            return
        if self.size[ra] < self.size[rb]:
            ra, rb = rb, ra
        self.parent[rb] = ra
        self.size[ra] += self.size[rb]

class Solution:
    def findAllPeople(self, n: int, meetings: List[List[int]], firstPerson: int) -> List[int]:
        # Time-optimized approach (common "best" solution):
        # For each time group:
        # 1) Union all edges in that time
        # 2) If a component contains a knower, mark whole component as knowers
        # 3) Reset DSU for participants in this time (unions do NOT carry over time)

        meetings.sort(key=lambda x: x[2])

        know = [False] * n
        know[0] = True
        know[firstPerson] = True

        dsu = DSU(n)
        m = len(meetings)
        i = 0

        while i < m:
            t = meetings[i][2]
            participants = []

            # Union all meetings at time t
            j = i
            while j < m and meetings[j][2] == t:
                x, y, _ = meetings[j]
                dsu.union(x, y)
                participants.append(x)
                participants.append(y)
                j += 1

            # Determine which roots at this time already have the secret
            good_roots = set()
            for p in participants:
                if know[p]:
                    good_roots.add(dsu.find(p))

            # Spread secret within those components
            for p in participants:
                if dsu.find(p) in good_roots:
                    know[p] = True

            # Reset DSU structure only for touched nodes (so next time is independent)
            for p in participants:
                dsu.parent[p] = p
                dsu.size[p] = 1

            i = j

        return [idx for idx, v in enumerate(know) if v]


if __name__ == "__main__":
    sol = Solution()
    print(sol.findAllPeople(6, [[1,2,5],[2,3,8],[1,5,10]], 1))
    print(sol.findAllPeople(4, [[3,1,3],[1,2,2],[0,3,3]], 3))
    print(sol.findAllPeople(5, [[3,4,2],[1,2,1],[2,3,1]], 1))
