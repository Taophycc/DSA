class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        ROWS, COLS = len(board),len(board[0])

        for c in range(COLS):
            if board[0][c] == 'O':
                board[0][c] = 'P'
            if board[ROWS - 1][c] == 'O':
                board[ROWS - 1][c] = 'P'

        for r in range(1, ROWS - 1):
            if board[r][0] == 'O':    
                board[r][0] = 'P'
            if board[r][COLS - 1] == 'O':
                board[r][COLS - 1] = 'P'

        directions = [(1,0), (-1,0),(0, 1),(0, -1)]
        def dfs(r,c):
            board[r][c] = 'P'

            for dr,dc in directions:
                nrow, ncol = dr + r, dc + c

                if 0 <= nrow < ROWS and 0 <= ncol < COLS and board[nrow][ncol] =='O':
                    dfs(nrow, ncol)

        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == 'P':
                    dfs(r,c)

        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == 'P':
                    board[r][c] ='O'
                elif board[r][c] == 'O':
                    board[r][c] = 'X'