# filename: longest_substring_bruteforce_n3.py
# Brute force: O(n^3) time, O(min(n, Σ)) space for the set in uniqueness check.
# Check every substring and test if it has all unique characters.

def length_of_longest_substring_bruteforce(s: str) -> int:
    n = len(s)
    ans = 0

    def is_unique(i: int, j: int) -> bool:
        seen = set()
        for k in range(i, j + 1):
            if s[k] in seen:
                return False
            seen.add(s[k])
        return True

    for i in range(n):
        for j in range(i, n):
            if is_unique(i, j):
                ans = max(ans, j - i + 1)
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
        out = length_of_longest_substring_bruteforce(s)
        print(f"bruteforce | input={s!r} -> {out} (expected={expected})")
