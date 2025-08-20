from typing import List

def max_area_two_pointer(height: List[int]) -> int:
    """
    Classic optimal solution: O(n) time, O(1) space.
    Start with two ends, move the pointer at the smaller height inward,
    because width always shrinks and only a taller line can improve area.
    """
    i, j = 0, len(height) - 1
    best = 0
    while i < j:
        hi, hj = height[i], height[j]
        width = j - i
        # area with current pair
        area = width * (hi if hi < hj else hj)
        if area > best:
            best = area
        # move the smaller-height pointer inward
        if hi <= hj:
            i += 1
        else:
            j -= 1
    return best

if __name__ == "__main__":
    print("Two-Pointer (Optimal)")
    print(max_area_two_pointer([1,8,6,2,5,4,8,3,7]))  # 49
    print(max_area_two_pointer([1,1]))                # 1
