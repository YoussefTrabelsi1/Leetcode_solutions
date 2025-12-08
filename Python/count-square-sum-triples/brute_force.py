# brute_force.py

def count_square_triples(n: int) -> int:
    """
    Brute-force O(n^3):
    Try all triples (a, b, c) with 1 <= a, b, c <= n
    and count those satisfying a^2 + b^2 = c^2.
    """
    count = 0
    for a in range(1, n + 1):
        for b in range(1, n + 1):
            for c in range(1, n + 1):
                if a * a + b * b == c * c:
                    count += 1
    return count


if __name__ == "__main__":
    # Simple manual tests
    print(count_square_triples(5))   # Expected 2
    print(count_square_triples(10))  # Expected 4
