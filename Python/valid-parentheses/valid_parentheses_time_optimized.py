# file: valid_parentheses_time_optimized.py

def is_valid_time_optimized(s: str) -> bool:
    """
    Time-optimal approach (standard solution):
    Use a stack and a hash map of closing -> opening bracket.
    Scan once from left to right.
    Time: O(n)
    Space: O(n) in worst case (all opening brackets)
    """
    pair = {
        ')': '(',
        ']': '[',
        '}': '{',
    }
    stack = []

    for ch in s:
        # If it's an opening bracket, push to stack
        if ch in "([{":
            stack.append(ch)
        else:
            # It's a closing bracket: stack must not be empty
            if not stack:
                return False
            # Top must match the corresponding opening bracket
            if stack[-1] != pair.get(ch, None):
                return False
            stack.pop()

    # Valid only if no unmatched opening brackets remain
    return not stack


# Simple tests
if __name__ == "__main__":
    tests = [
        ("()", True),
        ("()[]{}", True),
        ("(]", False),
        ("([])", True),
        ("([)]", False),
        ("(((", False),
        ("", False),  # outside constraints but good sanity check
    ]
    for t, expected in tests:
        print(t, is_valid_time_optimized(t), "expected:", expected)
