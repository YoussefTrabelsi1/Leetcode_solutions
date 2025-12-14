# time_optimized_seat_positions.py
MOD = 1_000_000_007


class Solution:
    def numberOfWays(self, corridor: str) -> int:
        seat_pos = [i for i, ch in enumerate(corridor) if ch == "S"]
        m = len(seat_pos)
        if m == 0 or (m & 1):
            return 0

        ways = 1
        # Pairs are (0,1), (2,3), (4,5), ...
        # For each boundary between pairs, multiply by distance between s_{2k-1} and s_{2k}
        for i in range(2, m, 2):
            ways = (ways * (seat_pos[i] - seat_pos[i - 1])) % MOD
        return ways


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
