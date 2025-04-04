class Solution:
    def findWords(self, board, words):
        ROWS, COLS = len(board), len(board[0])
        res = []

        def backtrack(r, c, i):
            if i == len(word):
                return True
            if (r < 0 or c < 0 or r >= ROWS or 
                c >= COLS or board[r][c] != word[i]
            ):
                return False

            board[r][c] = '*'
            ret = (backtrack(r + 1, c, i + 1) or
                   backtrack(r - 1, c, i + 1) or
                   backtrack(r, c + 1, i + 1) or
                   backtrack(r, c - 1, i + 1))
            board[r][c] = word[i]
            return ret

        for word in words:
            flag = False
            for r in range(ROWS):
                if flag:
                    break
                for c in range(COLS):
                    if board[r][c] != word[0]:
                        continue
                    if backtrack(r, c, 0):
                        res.append(word)
                        flag = True
                        break
        return res