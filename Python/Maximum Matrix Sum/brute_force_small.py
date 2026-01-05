# brute_force_small.py
from collections import deque
from typing import List


class Solution:
    """
    Brute force (ONLY practical for very small matrices).
    Uses BFS over reachable sign-flip masks by applying edge operations.

    If matrix is larger than 4x4, it automatically falls back to the optimal method.
    """

    def maximumMatrixSum(self, matrix: List[List[int]]) -> int:
        n = len(matrix)
        m = n * n
        if m > 16:  # brute-force cutoff
            return self._optimal(matrix)

        vals = [matrix[i][j] for i in range(n) for j in range(n)]

        # Build edge masks (adjacent pairs)
        edge_masks = []
        for i in range(n):
            for j in range(n):
                u = i * n + j
                if i + 1 < n:
                    v = (i + 1) * n + j
                    edge_masks.append((1 << u) ^ (1 << v))
                if j + 1 < n:
                    v = i * n + (j + 1)
                    edge_masks.append((1 << u) ^ (1 << v))

        # BFS from mask=0 (no flips applied)
        q = deque([0])
        seen = {0}
        best = -10**30

        while q:
            mask = q.popleft()

            s = 0
            for idx, a in enumerate(vals):
                if (mask >> idx) & 1:
                    s -= a
                else:
                    s += a
            if s > best:
                best = s

            for em in edge_masks:
                nm = mask ^ em
                if nm not in seen:
                    seen.add(nm)
                    q.append(nm)

        return best

    def _optimal(self, matrix: List[List[int]]) -> int:
        total_abs = 0
        min_abs = 10**18
        neg_count = 0
        has_zero = False

        for row in matrix:
            for x in row:
                if x == 0:
                    has_zero = True
                if x < 0:
                    neg_count += 1
                ax = -x if x < 0 else x
                total_abs += ax
                if ax < min_abs:
                    min_abs = ax

        if has_zero:
            return total_abs
        if neg_count % 2 == 0:
            return total_abs
        return total_abs - 2 * min_abs
