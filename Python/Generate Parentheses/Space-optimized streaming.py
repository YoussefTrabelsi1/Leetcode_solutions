from typing import Iterator, List

def iter_parentheses(n: int) -> Iterator[str]:
    """
    Generator version of backtracking: yields results one-by-one without storing all.
    Great when you want to stream/process combinations on the fly.
    Time:  O(C_n) total work
    Space: O(n) recursion; does NOT keep the full list in memory
    """
    curr: List[str] = [''] * (2 * n)

    def dfs(pos: int, open_used: int, close_used: int):
        if pos == 2 * n:
            yield ''.join(curr)
            return
        if open_used < n:
            curr[pos] = '('
            yield from dfs(pos + 1, open_used + 1, close_used)
        if close_used < open_used:
            curr[pos] = ')'
            yield from dfs(pos + 1, open_used, close_used + 1)

    return dfs(0, 0, 0)

# Example usage:
# for s in iter_parentheses(3):
#     print(s)
