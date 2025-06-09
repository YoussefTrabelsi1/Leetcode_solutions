class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1:
            return 1

        def matrix_mult(A, B):
            return [[A[0][0] * B[0][0] + A[0][1] * B[1][0], 
                     A[0][0] * B[0][1] + A[0][1] * B[1][1]],
                    [A[1][0] * B[0][0] + A[1][1] * B[1][0], 
                     A[1][0] * B[0][1] + A[1][1] * B[1][1]]]

        def matrix_pow(M, p):
            result = [[1, 0], [0, 1]]  
            base = M

            while p:
                if p % 2 == 1:
                    result = matrix_mult(result, base)
                base = matrix_mult(base, base)
                p //= 2

            return result

        M = [[1, 1], [1, 0]]
        result = matrix_pow(M, n)
        return result[0][0]