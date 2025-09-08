from typing import List, Dict, Tuple
from collections import defaultdict

def group_anagrams_time_optimized(strs: List[str]) -> List[List[str]]:
    """
    Optimal time approach:
      - Build a hash map from a 26-count tuple signature to list of words.
      - Each string contributes O(L) to build the signature.
    Time: O(n * L)
    Space: O(n) for grouping (plus small constant for signatures).
    """
    groups: Dict[Tuple[int, ...], List[str]] = defaultdict(list)
    base = ord('a')
    for s in strs:
        count = [0] * 26
        for ch in s:
            count[ord(ch) - base] += 1
        groups[tuple(count)].append(s)
    return list(groups.values())

# --- Demo ---
if __name__ == "__main__":
    print(group_anagrams_time_optimized(["eat","tea","tan","ate","nat","bat"]))
    print(group_anagrams_time_optimized([""]))
    print(group_anagrams_time_optimized(["a"]))
