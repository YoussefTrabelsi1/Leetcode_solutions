def strStr(haystack, needle):
    try:
        index= haystack.index(needle)
        return index
    except ValueError:
        return -1


haystack = "sadbutsad"
needle = "sad"

print(strStr(haystack, needle))

haystack = "leetcode"
needle = "leeto"

print(strStr(haystack, needle))
