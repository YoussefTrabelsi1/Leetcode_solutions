# filename: greedy_sort_optimal.py
def min_boxes_greedy_sort(apple, capacity):
    """
    Optimal greedy: only total apples matter (packs can be split),
    so pick largest box capacities until reaching the required total.
    Time: O(m log m), Space: O(1) extra (ignoring sort).
    """
    need = sum(apple)
    capacity.sort(reverse=True)

    cur = 0
    for i, c in enumerate(capacity, 1):
        cur += c
        if cur >= need:
            return i
    return len(capacity)  # guaranteed feasible by statement

if __name__ == "__main__":
    print(min_boxes_greedy_sort([1, 3, 2], [4, 3, 1, 5, 2]))  # 2
    print(min_boxes_greedy_sort([5, 5, 5], [2, 4, 2, 7]))     # 4
