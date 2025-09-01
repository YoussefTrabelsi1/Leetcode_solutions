# Solution 1 — Brute-force reduction (O(n^2) time, O(n) space)
# Repeatedly find the leftmost reducible pattern "int int op" and collapse it.

from typing import List, Union

def evalRPN_bruteforce(tokens: List[str]) -> int:
    # Convert numbers to ints; keep operators as strings
    t: List[Union[int, str]] = [int(x) if x not in {"+", "-", "*", "/"} else x for x in tokens]

    def apply(a: int, b: int, op: str) -> int:
        if op == "+": return a + b
        if op == "-": return a - b
        if op == "*": return a * b
        # Truncate toward zero
        return int(a / b)

    while len(t) > 1:
        # find first i where t[i-2], t[i-1] are ints and t[i] is an operator
        i = 0
        n = len(t)
        while i < n:
            if isinstance(t[i], str) and i >= 2 and isinstance(t[i-1], int) and isinstance(t[i-2], int):
                res = apply(t[i-2], t[i-1], t[i])
                # replace the triplet with the result
                t[i-2:i+1] = [res]
                break
            i += 1
    return t[0]

if __name__ == "__main__":
    print(evalRPN_bruteforce(["2","1","+","3","*"]))  # 9
    print(evalRPN_bruteforce(["4","13","5","/","+"]))  # 6
    print(evalRPN_bruteforce(["10","6","9","3","+","-11","*","/","*","17","+","5","+"]))  # 22
