# union_find_near_linear.py
# Union-Find / Disjoint Set Union (DSU) approach.
# Time: ~O(n α(n)) ≈ O(n) in practice; Space: O(n).
# Map each unique value to an index; union value with value+1 if both appear.

from typing import List, Dict

class DSU:
    def __init__(self, n: int):
        self.parent = list(range(n))
        self.size = [1] * n

    def find(self, x: int) -> int:
        while self.parent[x] != x:
            self.parent[x] = self.parent[self.parent[x]]  # path compression
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

def longest_consecutive_union_find(nums: List[int]) -> int:
    if not nums:
        return 0

    index_of: Dict[int, int] = {}
    idx = 0
    for v in nums:
        if v not in index_of:   # skip duplicates
            index_of[v] = idx
            idx += 1

    dsu = DSU(len(index_of))

    for v in index_of:
        if v + 1 in index_of:
            dsu.union(index_of[v], index_of[v + 1])

    # The length of the longest consecutive sequence corresponds to
    # the largest component size (since we union v with v+1 edges).
    best = 0
    # sizes are maintained at roots; ensure we check only roots or compute via finds
    for i in range(len(index_of)):
        if dsu.find(i) == i:
            if dsu.size[i] > best:
                best = dsu.size[i]
    return best

if __name__ == "__main__":
    print(longest_consecutive_union_find([100,4,200,1,3,2]))           # 4
    print(longest_consecutive_union_find([0,3,7,2,5,8,4,6,0,1]))       # 9
