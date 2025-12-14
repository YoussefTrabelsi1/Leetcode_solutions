# brute_force_with_fallback.py
from functools import lru_cache

MOD = 1_000_000_007


class Solution:
    def numberOfWays(self, corridor: str) -> int:
        n = len(corridor)

        # Brute force is exponential; keep it truly brute for small n,
        # and fall back to the optimal method for big inputs so the script is usable.
        if n <= 25:
            return self._bruteforce(corridor)
        return self._optimal_stream(corridor)

    def _bruteforce(self, corridor: str) -> int:
        n = len(corridor)

        @lru_cache(None)
        def dfs(i: int, seats_in_section: int) -> int:
            """
            We process corridor[i] next.
            Divider decisions are made AFTER placing corridor[i] into the current section,
            for i < n-1. Divider after the last char is forced (right boundary).
            """
            if i == n:
                return 0  # should never happen

            seats = seats_in_section + (1 if corridor[i] == "S" else 0)
            if seats > 2:
                return 0

            # Forced divider at the end
            if i == n - 1:
                return 1 if seats == 2 else 0

            # Option 1: no divider after i
            ways = dfs(i + 1, seats)

            # Option 2: place divider after i (only valid if section has exactly 2 seats)
            if seats == 2:
                ways += dfs(i + 1, 0)

            return ways % MOD

        return dfs(0, 0)

    def _optimal_stream(self, corridor: str) -> int:
        total_seats = corridor.count("S")
        if total_seats == 0 or (total_seats & 1):
            return 0

        pairs = total_seats // 2
        ways = 1

        seats_in_pair = 0
        pairs_done = 0
        prev_second = -1

        for idx, ch in enumerate(corridor):
            if ch != "S":
                continue

            # First seat of a new pair (after at least one pair completed)
            if pairs_done > 0 and seats_in_pair == 0:
                ways = (ways * (idx - prev_second)) % MOD

            seats_in_pair += 1
            if seats_in_pair == 2:
                prev_second = idx
                seats_in_pair = 0
                pairs_done += 1
                if pairs_done == pairs:
                    break

        return ways % MOD


if __name__ == "__main__":
    import sys

    s = sys.stdin.read().strip()
    if not s:
        tests = ["SSPPSPS", "PPSPSP", "S"]
        sol = Solution()
        for t in tests:
            print(t, "->", sol.numberOfWays(t))
    else:
        s = s.strip().strip('"').strip("'")
        print(Solution().numberOfWays(s))
