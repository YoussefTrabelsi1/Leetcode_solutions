from typing import List

def max_area_two_pointer_skip(height: List[int]) -> int:
    """
    Same O(n)/O(1) guarantees as the classic two-pointer, but when we move a pointer,
    we skip over consecutive heights that are <= the height we just left.
    This can't miss the optimum (those lines can't form a better area with the fixed opposite side),
    and it often saves iterations on flat/plateau regions.
    """
    i, j = 0, len(height) - 1
    best = 0
    while i < j:
        hi, hj = height[i], height[j]
        width = j - i
        area = width * (hi if hi < hj else hj)
        if area > best:
            best = area

        if hi <= hj:
            old = hi
            i += 1
            # skip plateaus that cannot help
            while i < j and height[i] <= old:
                i += 1
        else:
            old = hj
            j -= 1
            # skip plateaus that cannot help
            while i < j and height[j] <= old:
                j -= 1
    return best

if __name__ == "__main__":
    print("Two-Pointer with Plateau Skipping")
    print(max_area_two_pointer_skip([1,8,6,2,5,4,8,3,7]))  # 49
    print(max_area_two_pointer_skip([1,1]))                # 1
