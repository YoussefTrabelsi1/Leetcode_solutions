def longestCommonPrefix(strs):
    if not strs:
        return ""
    
    # Start with the first string as the prefix
    prefix = strs[0]
    
    for str in strs[1:]:
        while not str.startswith(prefix):
            prefix=prefix[:-1]
            if not prefix:
                return ""
    return prefix

# Test Cases
print(longestCommonPrefix(["flower", "flow", "flight"]))  # Output: "fl"
print(longestCommonPrefix(["dog", "racecar", "car"]))     # Output: ""
