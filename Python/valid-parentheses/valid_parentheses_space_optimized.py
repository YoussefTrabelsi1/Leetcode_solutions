# file: valid_parentheses_space_optimized.py

def is_valid_space_optimized(s: str) -> bool:
    """
    Space-optimized stack style:
    Still O(n) extra space in the worst case (you cannot do better asymptotically
    because you may need to remember all previous opens), but we:
      - Use a preallocated list as a manual stack
      - Avoid dictionaries; only use simple comparisons
    Time: O(n)
    Space: O(n) for the stack (minimal necessary)
    """
    n = len(s)
    # Manual stack using fixed-size list and an index
    stack = [None] * n
    top = -1  # empty stack

    for ch in s:
        # Opening brackets -> push
        if ch == '(' or ch == '[' or ch == '{':
            top += 1
            stack[top] = ch
        else:
            # Closing bracket -> stack must not be empty
            if top < 0:
                return False
            top_char = stack[top]
            # Check matching pair directly with if-conditions
            if ch == ')' and top_char != '(':
                return False
            if ch == ']' and top_char != '[':
                return False
            if ch == '}' and top_char != '{':
                return False
            top -= 1  # pop

    # Valid only if stack is empty
    return top == -1


# Simple tests
if __name__ == "__main__":
    tests = [
        ("()", True),
        ("()[]{}", True),
        ("(]", False),
        ("([])", True),
        ("([)]", False),
        ("(([]){})", True),
        ("(([]){})]", False),
    ]
    for t, expected in tests:
        print(t, is_valid_space_optimized(t), "expected:", expected)
