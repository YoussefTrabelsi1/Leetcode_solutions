# filename: bucket_counting_optimized.py

from typing import List

def last_stone_weight_bucket(stones: List[int]) -> int:
    """
    Optimized via counting (bucket) since 1 <= stone <= 100.
    Each smash pops the two current maxima by scanning down the small weight range.
    Time: O(W * smashes) with W <= 100 (tiny, effectively constant here); Space: O(W).
    """
    if not stones:
        return 0

    M = max(stones)
    count = [0] * (M + 1)
    for s in stones:
        count[s] += 1

    m = M  # current highest non-empty bucket

    def pop_max() -> int:
        nonlocal m
        while m > 0 and count[m] == 0:
            m -= 1
        if m == 0:
            return 0
        count[m] -= 1
        return m

    while True:
        a = pop_max()
        if a == 0:
            return 0
        b = pop_max()
        if b == 0:
            return a
        if a != b:
            diff = a - b if a > b else b - a
            count[diff] += 1
            if diff > m:
                m = diff  # update pointer if we created a heavier stone (can happen when a >> b)

if __name__ == "__main__":
    print(last_stone_weight_bucket([2,3,6,2,4]))  # 1
    print(last_stone_weight_bucket([1,2]))        # 1
