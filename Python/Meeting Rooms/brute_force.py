# filename: brute_force.py

from typing import List, Tuple

def can_attend_meetings_bruteforce(intervals: List[Tuple[int, int]]) -> bool:
    """
    Brute force O(n^2): check every pair for overlap.
    Non-conflict at boundary (e.g., (0,8) and (8,10)) is allowed.
    """
    n = len(intervals)
    for i in range(n):
        s1, e1 = intervals[i]
        for j in range(i + 1, n):
            s2, e2 = intervals[j]
            # Overlap iff both start before the other ends
            if s1 < e2 and s2 < e1:
                return False
    return True


if __name__ == "__main__":
    print(can_attend_meetings_bruteforce([(0,30),(5,10),(15,20)]))  # False
    print(can_attend_meetings_bruteforce([(5,8),(9,15)]))           # True
    print(can_attend_meetings_bruteforce([(0,8),(8,10)]))           # True
