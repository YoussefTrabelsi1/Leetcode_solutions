# filename: space_optimized_bfs_per_time.py
from typing import List, Dict
from collections import defaultdict, deque

class Solution:
    def findAllPeople(self, n: int, meetings: List[List[int]], firstPerson: int) -> List[int]:
        # Space-lean approach:
        # Sort by time, build ONLY the graph for that time, BFS from current knowers in that time.
        # No global adjacency stored.

        meetings.sort(key=lambda x: x[2])

        know = [False] * n
        know[0] = True
        know[firstPerson] = True

        m = len(meetings)
        i = 0
        while i < m:
            t = meetings[i][2]
            graph: Dict[int, List[int]] = defaultdict(list)
            participants = set()

            # Build subgraph for this exact time
            while i < m and meetings[i][2] == t:
                x, y, _ = meetings[i]
                graph[x].append(y)
                graph[y].append(x)
                participants.add(x)
                participants.add(y)
                i += 1

            # Multi-source BFS from participants who already know
            q = deque([p for p in participants if know[p]])
            seen = set(q)

            while q:
                u = q.popleft()
                for v in graph[u]:
                    if v not in seen:
                        seen.add(v)
                        q.append(v)

            # Everyone reachable from a knower within this time learns
            for p in seen:
                know[p] = True

        return [idx for idx, v in enumerate(know) if v]


if __name__ == "__main__":
    sol = Solution()
    print(sol.findAllPeople(6, [[1,2,5],[2,3,8],[1,5,10]], 1))
    print(sol.findAllPeople(4, [[3,1,3],[1,2,2],[0,3,3]], 3))
    print(sol.findAllPeople(5, [[3,4,2],[1,2,1],[2,3,1]], 1))
