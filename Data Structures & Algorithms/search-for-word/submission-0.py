class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        if not board or not board[0] or not word:
            return False

        ROWS = len(board)
        COLS = len(board[0])

        def dfs(r, c, index):
            if len(word) == index:
                return True

            if r < 0 or r >=ROWS or c < 0 or c >= COLS or board[r][c] != word[index]:
                return False

            temp = board[r][c]
            board[r][c] = "#"

            found = dfs(r+1, c, index+1) or dfs(r-1, c, index+1) or dfs(r, c+1, index+1) or dfs(r, c-1, index+1)

            board[r][c] = temp

            return found

        for row in range(ROWS):
            for col in range(COLS):
                if board[row][col] == word[0]:
                    if dfs(row, col, 0) == True:
                        return True

        return False
        