from typing import List

def max_area_bruteforce(height: List[int]) -> int:
    """
    Baseline O(n^2): try every pair (i, j) and take area = (j - i) * min(h[i], h[j]).
    """
    n = len(height)
    best = 0
    for i in range(n):
        hi = height[i]
        for j in range(i + 1, n):
            hj = height[j]
            width = j - i
            area = width * (hi if hi < hj else hj)
            if area > best:
                best = area
    return best

if __name__ == "__main__":
    print("Brute Force")
    print(max_area_bruteforce([1,8,6,2,5,4,8,3,7]))  # 49
    print(max_area_bruteforce([1,1]))                # 1
