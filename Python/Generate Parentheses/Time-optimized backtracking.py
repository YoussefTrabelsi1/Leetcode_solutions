from typing import List

def generate_parentheses_backtrack(n: int) -> List[str]:
    """
    Backtracking with pruning:
      - You can add '(' if open_used < n
      - You can add ')' if close_used < open_used
    Generates only valid prefixes → optimal up to output size.
    Time:  O(C_n) node visits (proportional to number of valid outputs)
    Space: O(n) recursion + O(C_n * n) for the output
    """
    res: List[str] = []
    curr = [''] * (2 * n)  # pre-allocate buffer to avoid string churn

    def dfs(pos: int, open_used: int, close_used: int) -> None:
        if pos == 2 * n:
            res.append(''.join(curr))
            return
        if open_used < n:
            curr[pos] = '('
            dfs(pos + 1, open_used + 1, close_used)
        if close_used < open_used:
            curr[pos] = ')' 
            dfs(pos + 1, open_used, close_used + 1)

    dfs(0, 0, 0)
    return res

# Example usage:
# print(generate_parentheses_backtrack(3))
