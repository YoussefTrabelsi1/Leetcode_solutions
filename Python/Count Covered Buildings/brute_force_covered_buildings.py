# filename: brute_force_covered_buildings.py

from typing import List, Tuple

def count_covered_buildings_bruteforce(n: int, buildings: List[List[int]]) -> int:
    """
    Brute-force: O(m^2) time, O(1) extra space.
    For each building, scan the whole list to find
    at least one building in each of the four directions.
    m = len(buildings)
    """
    m = len(buildings)
    # Convert to list of tuples to avoid repeated list indexing cost
    b_tuples: List[Tuple[int, int]] = [tuple(b) for b in buildings]
    covered = 0

    for i in range(m):
        x, y = b_tuples[i]
        has_left = has_right = has_up = has_down = False

        for j in range(m):
            if i == j:
                continue
            a, b = b_tuples[j]

            # Same row
            if a == x:
                if b < y:
                    has_left = True
                elif b > y:
                    has_right = True

            # Same column
            if b == y:
                if a < x:
                    has_up = True
                elif a > x:
                    has_down = True

            if has_left and has_right and has_up and has_down:
                covered += 1
                break

    return covered


if __name__ == "__main__":
    # Quick manual tests
    print(count_covered_buildings_bruteforce(3, [[1,2],[2,2],[3,2],[2,1],[2,3]]))  # 1
    print(count_covered_buildings_bruteforce(3, [[1,1],[1,2],[2,1],[2,2]]))        # 0
    print(count_covered_buildings_bruteforce(5, [[1,3],[3,2],[3,3],[3,5],[5,3]]))  # 1
