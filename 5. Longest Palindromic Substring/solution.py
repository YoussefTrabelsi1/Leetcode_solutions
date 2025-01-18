def isPalindrome(x): 
    # Check if a string is a palindrome
    if len(x) in [0, 1]:
        return True
    else:
        return x[0] == x[-1] and isPalindrome(x[1:-1])

def longestPalindrome(s):
    """
    :type s: str
    :rtype: str
    """
    max_length = 0
    result = ""

    for right in range(len(s)):
        for left in range(0, right + 1):
            substring = s[left:right + 1]
            if isPalindrome(substring):
                length = right - left + 1
                if length > max_length:
                    max_length = length
                    result = substring
    
    return result

# Test cases
s1 = "babad"
print(longestPalindrome(s1))  # Expected: "bab" or "aba"

s2 = "cbbd"
print(longestPalindrome(s2))  # Expected: "bb"
