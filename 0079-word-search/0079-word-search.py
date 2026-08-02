class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        n, m = len(board), len(board[0])
        visited = set()

        directions = [(1,0), (-1, 0), (0, 1), (0, -1)]
        def dfs(r, c, index):
            if index == len(word):
                return True

            if r < 0 or r >= n or c < 0 or c >= m or board[r][c] != word[index] or (r,c) in visited:
                return False

            visited.add((r,c))
            for dc, dr in directions:
                if dfs(dr + r, dc + c, index + 1):
                    return True

            visited.remove((r,c))
            return False
                
        for r in range(n):
            for c in range(m):
                if board[r][c] == word[0]:
                    if dfs(r, c, 0):
                        return True
        return False