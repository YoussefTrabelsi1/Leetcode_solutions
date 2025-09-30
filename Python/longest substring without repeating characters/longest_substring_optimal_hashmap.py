# filename: longest_substring_optimal_hashmap.py
# Optimal time (O(n)) using sliding window with a hashmap (dict) of last seen indices.
# Space: O(min(n, Σ)).
# Move the left boundary past the last occurrence of the current character.

def length_of_longest_substring(s: str) -> int:
    last = {}  # char -> last index seen
    left = 0
    ans = 0
    for right, ch in enumerate(s):
        if ch in last and last[ch] >= left:
            left = last[ch] + 1
        last[ch] = right
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
        ("abba", 2),
        ("tmmzuxt", 5),
        ("a b c a b!", 4),
    ]
    for s, expected in tests:
        out = length_of_longest_substring(s)
        print(f"optimal-hashmap | input={s!r} -> {out} (expected={expected})")
