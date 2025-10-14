# filename: min_stack_two_stacks.py
# Approach: Optimal Time (Two Stacks) — O(1) for all operations, O(n) extra space.

from typing import List

class MinStack:
    def __init__(self):
        self._vals: List[int] = []
        self._mins: List[int] = []  # _mins[i] is the min of _vals[:i+1]

    def push(self, val: int) -> None:
        self._vals.append(val)
        if not self._mins:
            self._mins.append(val)
        else:
            self._mins.append(val if val < self._mins[-1] else self._mins[-1])

    def pop(self) -> None:
        self._vals.pop()
        self._mins.pop()

    def top(self) -> int:
        return self._vals[-1]

    def getMin(self) -> int:
        return self._mins[-1]


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
