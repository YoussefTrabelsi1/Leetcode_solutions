# filename: longest_substring_optimal_array.py
# Optimal time (O(n)) using sliding window with an array for ASCII last positions.
# Faster in practice than dict for ASCII inputs.
# Space: O(256). If input includes only ASCII (as per constraints), this is safe.

def length_of_longest_substring_ascii(s: str) -> int:
    # initialize to -1 for "not seen"
    last = [-1] * 256
    left = 0
    ans = 0
    for right, ch in enumerate(s):
        code = ord(ch)
        code = code if code < 256 else 255  # bucket any non-ASCII to 255 (conservative)
        if last[code] >= left:
            left = last[code] + 1
        last[code] = right
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
        ("!@# $%^&*()_+", 13),
    ]
    for s, expected in tests:
        out = length_of_longest_substring_ascii(s)
        print(f"optimal-array | input={s!r} -> {out} (expected={expected})")
