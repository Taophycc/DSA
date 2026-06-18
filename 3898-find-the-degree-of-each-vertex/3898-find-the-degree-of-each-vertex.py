class Solution:
    def findDegrees(self, matrix: list[list[int]]) -> list[int]:
        n, m = len(matrix), len(matrix[0])
        arr = []

        for i in range(n):
            cnt = 0
            for j in range(m):
                if matrix[i][j] == 1:
                    cnt += 1       
        
            arr.append(cnt)
        return arr