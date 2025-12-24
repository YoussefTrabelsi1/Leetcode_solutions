# filename: greedy_counting_time_optimized.py
def min_boxes_greedy_counting(apple, capacity):
    """
    Same optimal greedy idea, but avoids sorting using counting (capacity[i] <= 50).
    Time: O(m + 50), Space: O(50).
    """
    need = sum(apple)
    freq = [0] * 51
    for c in capacity:
        freq[c] += 1

    cur = 0
    used = 0
    for cap in range(50, 0, -1):
        while freq[cap] > 0 and cur < need:
            cur += cap
            used += 1
            freq[cap] -= 1
        if cur >= need:
            return used
    return len(capacity)

if __name__ == "__main__":
    print(min_boxes_greedy_counting([1, 3, 2], [4, 3, 1, 5, 2]))  # 2
    print(min_boxes_greedy_counting([5, 5, 5], [2, 4, 2, 7]))     # 4
