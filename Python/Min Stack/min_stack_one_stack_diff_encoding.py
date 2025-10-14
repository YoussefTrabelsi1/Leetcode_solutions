# filename: min_stack_one_stack_diff_encoding.py
# Approach: Space-Optimized (Single Stack + Diff Encoding)
# O(1) for all operations, O(1) extra space beyond stored elements.
# Idea:
#   Store differences d = val - current_min in the stack.
#   Maintain current minimum separately.
#   On push:
#       if empty: push 0, set min = val
#       else: push d; if d < 0, update min = val
#   On pop:
#       if popped d < 0, previous_min = current_min - d
#   On top:
#       if d >= 0: top = min + d
#       else: top = min  (since current_min == actual top when d < 0)

from typing import List

class MinStack:
    def __init__(self):
        self._s: List[int] = []
        self._min: int | None = None

    def push(self, val: int) -> None:
        if not self._s:
            self._s.append(0)
            self._min = val
        else:
            d = val - self._min  # may overflow in other langs; Python ints are unbounded
            self._s.append(d)
            if d < 0:
                # new value becomes the new minimum
                self._min = val

    def pop(self) -> None:
        d = self._s.pop()
        if d < 0:
            # popped element was the minimum; restore previous minimum
            # previous_min = current_min - d  (since d = val - prev_min and val == current_min)
            self._min = self._min - d
        if not self._s:
            self._min = None

    def top(self) -> int:
        d = self._s[-1]
        if d >= 0:
            return self._min + d
        else:
            return self._min

    def getMin(self) -> int:
        return self._min


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
