# Solution 3 — In-place space-optimized (O(n) time, O(1) extra space)
# Reuses the input list as a value stack via a write pointer. Mutates tokens.

from typing import List

def evalRPN_inplace(tokens: List[str]) -> int:
    w = 0  # write pointer: next slot for a value
    for tok in tokens:
        if tok == "+":
            b, a = tokens[w-1], tokens[w-2]
            tokens[w-2] = a + b
            w -= 1
        elif tok == "-":
            b, a = tokens[w-1], tokens[w-2]
            tokens[w-2] = a - b
            w -= 1
        elif tok == "*":
            b, a = tokens[w-1], tokens[w-2]
            tokens[w-2] = a * b
            w -= 1
        elif tok == "/":
            b, a = tokens[w-1], tokens[w-2]
            tokens[w-2] = int(a / b)  # truncates toward zero
            w -= 1
        else:
            # convert to int and store in-place
            tokens[w] = int(tok)
            w += 1
    return tokens[0]

if __name__ == "__main__":
    print(evalRPN_inplace(["2","1","+","3","*"]))  # 9
    print(evalRPN_inplace(["4","13","5","/","+"]))  # 6
    print(evalRPN_inplace(["10","6","9","3","+","-11","*","/","*","17","+","5","+"]))  # 22
