# file: brute_force.py
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
    # O(n^2): for each unique candidate, count occurrences by scanning.
    for x in nums:
        cnt = 0
        for y in nums:
            if y == x:
                cnt += 1
        if cnt > 1:  # given constraints, the only repeated value is the answer
            return x
    return None

def main():
    nums = parse_nums(sys.stdin.read())
    ans = repeated_n_times(nums)
    if ans is not None:
        print(ans)

if __name__ == "__main__":
    main()
