from typing import List

def daily_temperatures_const_space(temperatures: List[int]) -> List[int]:
    n = len(temperatures)
    result = [0] * n
    INF = 10**9
    # next_idx[t] = nearest index to the right where temperature == t (or INF if none)
    next_idx = [INF] * 101  # temps in [1..100]

    for i in range(n - 1, -1, -1):
        t = temperatures[i]
        # Find nearest warmer day among temps (t+1 .. 100)
        nearest = INF
        for warmer in range(t + 1, 101):
            if next_idx[warmer] < nearest:
                nearest = next_idx[warmer]
        result[i] = 0 if nearest == INF else nearest - i
        # Update where we last saw temperature t
        next_idx[t] = i
    return result

# Demo
if __name__ == "__main__":
    print(daily_temperatures_const_space([30,38,30,36,35,40,28]))  # [1,4,1,2,1,0,0]
    print(daily_temperatures_const_space([22,21,20]))              # [0,0,0]
