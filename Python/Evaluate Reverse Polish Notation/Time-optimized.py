# Solution 2 — Time-optimized stack (O(n) time, O(n) space)
# Minimizes overhead by avoiding dict lookups and binding stack ops locally.

from typing import List

def evalRPN_fast(tokens: List[str]) -> int:
    st: List[int] = []
    push, pop = st.append, st.pop
    for tok in tokens:
        if tok == "+":
            b, a = pop(), pop()
            push(a + b)
        elif tok == "-":
            b, a = pop(), pop()
            push(a - b)
        elif tok == "*":
            b, a = pop(), pop()
            push(a * b)
        elif tok == "/":
            b, a = pop(), pop()
            push(int(a / b))  # truncates toward zero
        else:
            push(int(tok))
    return st[0]

if __name__ == "__main__":
    print(evalRPN_fast(["2","1","+","3","*"]))  # 9
    print(evalRPN_fast(["4","13","5","/","+"]))  # 6
    print(evalRPN_fast(["10","6","9","3","+","-11","*","/","*","17","+","5","+"]))  # 22
