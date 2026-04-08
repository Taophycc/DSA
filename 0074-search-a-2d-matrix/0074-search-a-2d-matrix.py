class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        arr = []
        mp =  {}

        for i in range(len(matrix)):
            mp[matrix[i][0]] = i
            mp[matrix[i][-1]] = i
            arr.append(matrix[i][0])
            arr.append(matrix[i][-1])

        
        l, r = 0, len(arr) -1
        row_idx = 0

        while l <= r:
            mid = (l+r)//2

            if arr[mid] == target:
                return True
            elif arr[mid] < target:
                row_idx = mp[arr[mid]]
                l = mid +1
            else:
                r = mid - 1

        if row_idx != -1:
            x = row_idx
            a, b = 0, len(matrix[x]) -1

            while a <= b:
                mid = (a + b)//2
                if matrix[x][mid] == target:
                    return True
                elif matrix[x][mid] < target:
                    a = mid +1
                else:
                    b = mid - 1
        return False