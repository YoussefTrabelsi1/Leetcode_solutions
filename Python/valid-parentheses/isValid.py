def isValid(s):

    bracket_map = {')': '(', '}': '{', ']': '['}
    stack = []
    for char in s:
        if char not in bracket_map:
            stack.append(char)
        else:
            top_element=stack.pop() if stack else "#"

            if top_element!=bracket_map[char]:
                return False
            
            
    return not stack


print(isValid("()"))
print(isValid("()[]{}"))
print(isValid("(]"))
print(isValid("([])"))
