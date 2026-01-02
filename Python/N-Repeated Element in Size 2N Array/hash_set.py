# file: hash_set.py
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
    seen = set()
    for x in nums:
        if x in seen:
            return x
        seen.add(x)
    return None

def main():
    nums = parse_nums(sys.stdin.read())
    ans = repeated_n_times(nums)
    if ans is not None:
        print(ans)

if __name__ == "__main__":
    main()
