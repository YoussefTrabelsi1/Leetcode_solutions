from typing import List

def group_anagrams_space_optimized(strs: List[str]) -> List[List[str]]:
    """
    Brute force but space-optimized:
      - Avoids sorting in comparisons; uses fixed-size (26) frequency counts.
      - Still compares each pair, but each check is O(L) instead of O(L log L).
    Time: O(n^2 * L)
    Space: O(1) extra (excluding output and visited flags).
    """
    n = len(strs)
    visited = [False] * n
    res = []

    def is_anagram_by_count(a: str, b: str) -> bool:
        if len(a) != len(b):
            return False
        cnt = [0] * 26
        base = ord('a')
        for ch in a:
            cnt[ord(ch) - base] += 1
        for ch in b:
            idx = ord(ch) - base
            cnt[idx] -= 1
            if cnt[idx] < 0:
                return False
        # If all zeros, they're anagrams
        return all(x == 0 for x in cnt)

    for i in range(n):
        if visited[i]:
            continue
        group = [strs[i]]
        visited[i] = True
        for j in range(i + 1, n):
            if not visited[j] and is_anagram_by_count(strs[i], strs[j]):
                group.append(strs[j])
                visited[j] = True
        res.append(group)
    return res

# --- Demo ---
if __name__ == "__main__":
    print(group_anagrams_space_optimized(["eat","tea","tan","ate","nat","bat"]))
    print(group_anagrams_space_optimized([""]))
    print(group_anagrams_space_optimized(["a"]))
