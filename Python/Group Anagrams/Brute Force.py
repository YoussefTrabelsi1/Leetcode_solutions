from typing import List

def group_anagrams_bruteforce_sorted(strs: List[str]) -> List[List[str]]:
    """
    Brute force grouping:
      - For each string, compare with all ungrouped strings.
      - Two strings are anagrams if their sorted forms are equal.
    Time: O(n^2 * L log L)  (sorting within pair checks)
    Space: O(1) extra (excluding output and visited flags).
    """
    n = len(strs)
    visited = [False] * n
    res = []

    def is_anagram_by_sort(a: str, b: str) -> bool:
        return sorted(a) == sorted(b)

    for i in range(n):
        if visited[i]:
            continue
        group = [strs[i]]
        visited[i] = True
        for j in range(i + 1, n):
            if not visited[j] and is_anagram_by_sort(strs[i], strs[j]):
                group.append(strs[j])
                visited[j] = True
        res.append(group)
    return res

# --- Demo ---
if __name__ == "__main__":
    print(group_anagrams_bruteforce_sorted(["eat","tea","tan","ate","nat","bat"]))
    print(group_anagrams_bruteforce_sorted([""]))
    print(group_anagrams_bruteforce_sorted(["a"]))
