def isPalindrome(x):
    # Negative numbers and numbers ending with 0 (except 0 itself) are not palindromes
    if x < 0 or (x % 10 == 0 and x != 0):
        return False
    
    reversed_half = 0
    while x > reversed_half:
        # Add the last digit to reversed_half
        reversed_half = reversed_half * 10 + x % 10
        # Remove the last digit from x
        x //= 10
    
    # Check if either the full reversed half matches, or if it's the same ignoring the middle digit (for odd lengths)
    return x == reversed_half or x == reversed_half // 10

print(isPalindrome(121))
print(isPalindrome(-121))
print(isPalindrome(10))
print(isPalindrome(110))
