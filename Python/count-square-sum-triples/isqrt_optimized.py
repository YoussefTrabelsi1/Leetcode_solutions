# isqrt_optimized.py

from math import isqrt


def count_square_triples(n: int) -> int:
    """
    Time-optimized O(n^2):
    Loop over (a, b), compute c^2 = a^2 + b^2 and check if it's a perfect square
    with c <= n using integer square root.
    """
    count = 0
    for a in range(1, n + 1):
        aa = a * a
        for b in range(1, n + 1):
            c2 = aa + b * b
            c = isqrt(c2)
            if c <= n and c * c == c2:
                count += 1
    return count


if __name__ == "__main__":
    print(count_square_triples(5))   # Expected 2
    print(count_square_triples(10))  # Expected 4
