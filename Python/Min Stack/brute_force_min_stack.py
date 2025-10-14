# filename: brute_force_min_stack.py
# Approach: Brute Force (O(1) push/pop/top, O(n) getMin)

from typing import List

class MinStack:
    def __init__(self):
        self._s: List[int] = []

    def push(self, val: int) -> None:
        self._s.append(val)

    def pop(self) -> None:
        self._s.pop()

    def top(self) -> int:
        return self._s[-1]

    def getMin(self) -> int:
        # O(n) scan for the minimum
        return min(self._s)


if __name__ == "__main__":
    # Example run matching the prompt
    ops = ["MinStack","push","push","push","getMin","pop","top","getMin"]
    args = [[],[-2],[0],[-3],[],[],[],[]]
    out = []
    ms = None
    for op, arg in zip(ops, args):
        if op == "MinStack":
            ms = MinStack()
            out.append(None)
        elif op == "push":
            ms.push(arg[0])
            out.append(None)
        elif op == "pop":
            ms.pop()
            out.append(None)
        elif op == "top":
            out.append(ms.top())
        elif op == "getMin":
            out.append(ms.getMin())
    print(out)
