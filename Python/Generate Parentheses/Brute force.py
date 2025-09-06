from typing import List

def generate_parentheses_bruteforce(n: int) -> List[str]:
    """
    Brute force: enumerate all length-2n strings over {'(', ')'} and filter by validity.
    Time:  O(2^(2n)) to enumerate, with O(2n) validation each
    Space: O(C_n * n) for the output, O(1) extra (besides building each candidate)
    """
    def is_valid(s: str) -> bool:
        bal = 0
        for ch in s:
            bal += 1 if ch == '(' else -1
            if bal < 0:  # too many ')'
                return False
        return bal == 0

    res = []
    L = 2 * n
    # Iterate integers 0..(2^(2n)-1), where bit=1 -> '(' and bit=0 -> ')'
    for mask in range(1 << L):
        s = []
        for i in range(L):
            if (mask >> i) & 1:
                s.append('(')
            else:
                s.append(')')
        cand = ''.join(s)
        if is_valid(cand):
            res.append(cand)
    return res

# Example usage:
# print(generate_parentheses_bruteforce(3))
