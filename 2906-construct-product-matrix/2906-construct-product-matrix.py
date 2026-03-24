class Solution:
    def constructProductMatrix(self, grid: List[List[int]]) -> List[List[int]]:
        n,m = len(grid), len(grid[0])
        mod = 12345
        res = [[0]*m for _ in range(n)]

        suffix = 1
        for i in range(n-1, -1,-1):
            for j in range(m-1, -1, -1):
                res[i][j] = suffix
                suffix = (suffix * grid[i][j]) % mod
        
        prefix = 1
        for i in range(n):
            for j in range(m):
                res[i][j] = (res[i][j] * prefix) % mod
                prefix = (prefix * grid[i][j]) % mod

        return res
        

