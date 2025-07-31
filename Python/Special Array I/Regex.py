import re

def is_special(nums):
    s = ''.join(str(x % 2) for x in nums)
    return not re.search(r'00|11', s)
