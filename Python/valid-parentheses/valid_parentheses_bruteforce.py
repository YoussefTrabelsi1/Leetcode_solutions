# file: valid_parentheses_bruteforce.py

def is_valid_bruteforce(s: str) -> bool:
    """
    Brute-force approach:
    Repeatedly remove all occurrences of valid pairs "()", "[]", "{}"
    until the string stops changing. If we end up with an empty string,
    it was valid.
    Time: O(n^2) in worst case (many passes over the string)
    Space: O(n) for intermediate strings
    """
    # Keep shortening the string by removing valid pairs
    while True:
        new_s = s.replace("()", "").replace("[]", "").replace("{}", "")
        if new_s == s:
            break
        s = new_s
    return s == ""


# Simple tests
if __name__ == "__main__":
    tests = [
        ("()", True),
        ("()[]{}", True),
        ("(]", False),
        ("([])", True),
        ("([)]", False),
    ]
    for t, expected in tests:
        print(t, is_valid_bruteforce(t), "expected:", expected)
