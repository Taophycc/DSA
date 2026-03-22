class Solution:
    def findRotation(self, mat: List[List[int]], target: List[List[int]]) -> bool:
        n = len(mat)

        # 4 rotation rule, max no of rotations before going back to original matrix
        for _ in range(4):
            if mat == target:
                return True

            # transpose matrix
            for r in range(n):
                for c in range(r+1, n):
                    mat[r][c], mat[c][r] = mat[c][r], mat[r][c]

            # reverse rows
            for i in range(n):
                mat[i].reverse()

      
        return False

