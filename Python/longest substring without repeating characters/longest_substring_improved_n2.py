# filename: longest_substring_improved_n2.py
# Improved brute force / expanding window per start index: O(n^2) time, O(min(n, Σ)) space.
# For each left index, expand right until a duplicate appears, using a set.

def length_of_longest_substring_n2(s: str) -> int:
    n = len(s)
    ans = 0
    for left in range(n):
        seen = set()
        for right in range(left, n):
            c = s[right]
            if c in seen:
                break
            seen.add(c)
            ans = max(ans, right - left + 1)
    return ans


if __name__ == "__main__":
    tests = [
        ("abcabcbb", 3),
        ("bbbbb", 1),
        ("pwwkew", 3),
        ("", 0),
        ("au", 2),
        ("dvdf", 3),
        ("anviaj", 5),
    ]
    for s, expected in tests:
        out = length_of_longest_substring_n2(s)
        print(f"n2-improved | input={s!r} -> {out} (expected={expected})")
