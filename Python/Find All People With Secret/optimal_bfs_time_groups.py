# filename: optimal_bfs_time_groups.py
from typing import List, Dict
from collections import defaultdict, deque

class Solution:
    def findAllPeople(self, n: int, meetings: List[List[int]], firstPerson: int) -> List[int]:
        # "Optimal" in practice: O(m log m) sorting + O(m) processing.
        # Similar to the space-optimized BFS, but written cleanly and efficiently.

        meetings.sort(key=lambda x: x[2])
        know = [False] * n
        know[0] = True
        know[firstPerson] = True

        i, m = 0, len(meetings)
        while i < m:
            t = meetings[i][2]
            graph: Dict[int, List[int]] = defaultdict(list)
            nodes = set()

            while i < m and meetings[i][2] == t:
                x, y, _ = meetings[i]
                graph[x].append(y)
                graph[y].append(x)
                nodes.add(x)
                nodes.add(y)
                i += 1

            q = deque()
            visited = set()
            for u in nodes:
                if know[u]:
                    q.append(u)
                    visited.add(u)

            while q:
                u = q.popleft()
                for v in graph[u]:
                    if v not in visited:
                        visited.add(v)
                        q.append(v)

            for u in visited:
                know[u] = True

        return [i for i, v in enumerate(know) if v]


if __name__ == "__main__":
    sol = Solution()
    print(sol.findAllPeople(6, [[1,2,5],[2,3,8],[1,5,10]], 1))
    print(sol.findAllPeople(4, [[3,1,3],[1,2,2],[0,3,3]], 3))
    print(sol.findAllPeople(5, [[3,4,2],[1,2,1],[2,3,1]], 1))
