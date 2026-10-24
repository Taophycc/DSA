class Solution:
    def updateBoard(self, board: List[List[str]], click: List[int]) -> List[List[str]]:
        r, c = click[0], click[1]
        if board[r][c] == "M":
            board[r][c] = "X"
            return board
        
        rows, cols = len(board), len(board[0])
        directions = [(-1, -1), (-1, 0),(-1, 1),( 0, -1),(0, 1),( 1, -1), ( 1, 0), ( 1, 1)]
        queue = deque([(r, c)])
        board[r][c] = "B"

        while queue:
            r,c = queue.popleft()

            mine_count = 0
            unrevealed_neighbors = []

            for dr, dc in directions:
                nr, nc = dr + r, dc + c
                if 0 <= nr < rows and 0 <= nc < cols:
                    if board[nr][nc] == "M":
                        mine_count += 1
                    elif board[nr][nc] == "E":
                        unrevealed_neighbors.append((nr,nc))
            
            if mine_count > 0:
                board[r][c] = str(mine_count)
            else:
                for nr , nc in unrevealed_neighbors:
                    board[nr][nc] = "B" 
                    queue.append((nr, nc))
            
        return board