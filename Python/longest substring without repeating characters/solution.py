def lengthOfLongestSubstring(s):
    """
    :type s: str
    :rtype: int
    """
    char_set=set() # substring set
    max_length=0
    left=0 # Position of left pointer

    for right in range(len(s)):
        #check if caracter is in the substring
        while s[right] in char_set:
            #remove the characters from the left pointer and move the pointer until the set doesn t contain duplicate elements
            char_set.remove(s[left])
            left+=1
        
        char_set.add(s[right])

        max_length=max(max_length,right-left+1)

    return max_length


s = "abcabcbb"

print(lengthOfLongestSubstring(s))

s = "bbbbbbbbb"

print(lengthOfLongestSubstring(s))

s = "pwwkew"

print(lengthOfLongestSubstring(s))
