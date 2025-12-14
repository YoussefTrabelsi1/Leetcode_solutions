# space_optimized_single_pass.py
MOD = 1_000_000_007


class Solution:
    def numberOfWays(self, corridor: str) -> int:
        total_seats = corridor.count("S")
        if total_seats == 0 or (total_seats & 1):
            return 0

        pairs = total_seats // 2
        ways = 1

        seats_in_pair = 0
        pairs_done = 0
        prev_second = -1  # index of the 2nd seat of the previous completed pair

        for idx, ch in enumerate(corridor):
            if ch != "S":
                continue

            # Starting a new pair after finishing at least one pair => multiply gap choices
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
