def isPalindrome(x):
    # Negative numbers and numbers ending with 0 (except 0 itself) are not palindromes
    if x<0  or (x % 10 == 0 and x != 0):
        return False
    
    reversed=0
    while reversed<x:

        reversed=10*reversed + x%10
        x//=10
    print(reversed)
    
    return x==reversed or x == reversed//10


print(isPalindrome(121))
print(isPalindrome(-121))
print(isPalindrome(10))
print(isPalindrome(110))
