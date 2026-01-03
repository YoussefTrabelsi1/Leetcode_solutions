# paint_grid_matrix_exp.py
# Time-optimized asymptotically: O(log n) using matrix exponentiation on the 2-state recurrence.

import sys

MOD = 10**9 + 7

def mat_mul(A, B):
    return [
        [(A[0][0] * B[0][0] + A[0][1] * B[1][0]) % MOD,
         (A[0][0] * B[0][1] + A[0][1] * B[1][1]) % MOD],
        [(A[1][0] * B[0][0] + A[1][1] * B[1][0]) % MOD,
         (A[1][0] * B[0][1] + A[1][1] * B[1][1]) % MOD],
    ]

def mat_pow(M, e: int):
    # 2x2 identity
    R = [[1, 0], [0, 1]]
    while e > 0:
        if e & 1:
            R = mat_mul(R, M)
        M = mat_mul(M, M)
        e >>= 1
    return R

def mat_vec(M, v):
    return [
        (M[0][0] * v[0] + M[0][1] * v[1]) % MOD,
        (M[1][0] * v[0] + M[1][1] * v[1]) % MOD,
    ]

def num_of_ways_matrix(n: int) -> int:
    # [two_next]   [3 2] [two]
    # [three_next]= [2 2] [three]
    if n == 1:
        return 12

    base = [6, 6]  # [two, three] at row 1
    T = [[3, 2], [2, 2]]
    P = mat_pow(T, n - 1)
    res = mat_vec(P, base)
    return (res[0] + res[1]) % MOD

def solve() -> None:
    data = sys.stdin.read().strip().split()
    n = int(data[0]) if data else 1
    print(num_of_ways_matrix(n))

if __name__ == "__main__":
    solve()
