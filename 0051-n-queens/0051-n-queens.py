class Solution:
    def solveNQueens(self, n: int) -> list[list[str]]:
        # Put them one row at a time, without looking at the columns.
        ans = []
        # col[r]:In which column is the queen of row r placed?
        col = [0] * n

        # R,C:The row and column numbers that have been placed before
        # r,c:Now prepare the row and column number to be placed
        def valid(r, c):
            for R in range(r):
                C = col[R]
                if r + c == R + C or r - c == R - C:
                    return False
            return True

        # r:Which row should put
        # s:rest column
        def dfs(r, s):
            # 把col[]翻译成棋盘格式
            if r == n:
                board = []
                for c in col:
                    # 先create all . then change Q '.','Q','.','.'
                    row = ["."] * n
                    row[c] = "Q"
                    # 拼成字符串".Q.."
                    board.append("".join(row))
                ans.append(board)
                return

            for c in s:
                if valid(r, c):
                    col[r] = c
                    dfs(r + 1, s - {c})

        dfs(0, set(range(n)))
        return ans

