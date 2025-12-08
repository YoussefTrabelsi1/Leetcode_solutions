# euclid_number_theory.py

from math import gcd, isqrt


def count_square_triples(n: int) -> int:
    """
    Number-theoretic / Euclid formula approach.
    Generate all primitive Pythagorean triples (a, b, c) with:
        a = m^2 - n^2
        b = 2mn
        c = m^2 + n^2
    where m > n, gcd(m, n) = 1, (m - n) is odd.
    Then scale by k while k * c <= n.
    Each (a, b, c) gives two ordered triples: (a, b, c) and (b, a, c).
    Overall complexity ~ O(sqrt(n)^2 * log n) in practice much faster than O(n^2).
    """
    count = 0
    max_m = isqrt(n) + 1  # Rough upper bound on m

    for m in range(2, max_m + 1):
        for nn in range(1, m):
            # c for primitive triple
            c = m * m + nn * nn
            if c > n:
                # For larger nn, c only increases, so break inner loop
                break

            # Conditions for primitive triple
            if gcd(m, nn) != 1:
                continue
            if (m - nn) % 2 == 0:
                continue

            a = m * m - nn * nn
            b = 2 * m * nn

            # Scale primitive triple by k
            k = 1
            while k * c <= n:
                # Each scaled triple (ka, kb, kc) is valid with ka, kb, kc <= n
                # Count ordered pairs: (ka, kb, kc) and (kb, ka, kc)
                count += 2
                k += 1

    return count


if __name__ == "__main__":
    print(count_square_triples(5))   # Expected 2
    print(count_square_triples(10))  # Expected 4
