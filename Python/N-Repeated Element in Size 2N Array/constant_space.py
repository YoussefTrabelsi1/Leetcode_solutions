# file: constant_space.py
import sys
import ast
import re

def parse_nums(s: str):
    s = s.strip()
    if not s:
        return []
    try:
        v = ast.literal_eval(s)
        if isinstance(v, list):
            return v
    except Exception:
        pass
    return list(map(int, re.findall(r"-?\d+", s)))

def repeated_n_times(nums):
    m = len(nums)
    # Check offsets 1..3; guaranteed to find the repeated element.
    for i in range(m - 1):
        if nums[i] == nums[i + 1]:
            return nums[i]
    for i in range(m - 2):
        if nums[i] == nums[i + 2]:
            return nums[i]
    for i in range(m - 3):
        if nums[i] == nums[i + 3]:
            return nums[i]
    return None

def main():
    nums = parse_nums(sys.stdin.read())
    ans = repeated_n_times(nums)
    if ans is not None:
        print(ans)

if __name__ == "__main__":
    main()
