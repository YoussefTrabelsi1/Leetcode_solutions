# filename: brute_force_scan.py

from typing import List

def last_stone_weight_bruteforce(stones: List[int]) -> int:
    """
    Brute force: repeatedly scan the array to find the two heaviest stones.
    Time: O(n^2) for n up to 20 (small); Space: O(1) extra aside from the working list.
    """
    arr = stones[:]  # work on a copy
    while len(arr) > 1:
        # Find index of the heaviest stone
        i1 = max(range(len(arr)), key=arr.__getitem__)
        first = arr.pop(i1)
        # Find index of the second heaviest stone
        i2 = max(range(len(arr)), key=arr.__getitem__)
        second = arr.pop(i2)
        # Smash
        if first != second:
            arr.append(abs(first - second))
    return arr[0] if arr else 0


if __name__ == "__main__":
    print(last_stone_weight_bruteforce([2,3,6,2,4]))  # 1
    print(last_stone_weight_bruteforce([1,2]))        # 1
