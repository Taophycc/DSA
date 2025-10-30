# Difficulty - EASY 

    # def countNegatives(self, grid: List[List[int]]) -> int:
    #     rows = len(grid)
    #     cols = len(grid[0])
        
    #     current_row = 0
    #     current_col = cols - 1
        
    #     count = 0
        
    #     while current_row < rows and current_col >= 0:
            
    #         if grid[current_row][current_col] < 0:
                
    #             count += (rows - current_row)
    #             current_col -= 1
                
    #         else:
    #             current_row += 1
                
    #     return count

'''
Intuition:
The problem asks us to count the number of negative numbers in a matrix that is sorted in non-increasing order both row-wise and column-wise.
A naive approach would be to iterate through each element of the matrix and check if it's negative, which would take O(m*n) time.
We can do better. Since the matrix is sorted, we can use a more efficient search pattern.

Let's start from the top-right corner of the matrix. Let's say this position is `(row, col)`.
- If `grid[row][col]` is negative, then all the elements in the current column below it are also negative (because the column is sorted in non-increasing order). So, we add `(rows - row)` to our count and move to the previous column (`col - 1`) to find more negative numbers.
- If `grid[row][col]` is non-negative, then all the elements in the current row to its left are also non-negative. So, we can safely move to the next row (`row + 1`) to find negative numbers.

We continue this process until we are out of the matrix bounds.

Example Walkthrough:
Let's say the grid is:
[[ 4,  3,  2, -1],
 [ 3,  2,  1, -1],
 [ 1,  1, -1, -2],
 [-1, -1, -2, -3]]

1. Start at `(0, 3)`. `grid[0][3]` is -1 (negative).
   - All elements below it are also negative. There are `4 - 0 = 4` rows from here. So, `count = 4`.
   - Move to the previous column: `col = 2`.
2. Now at `(0, 2)`. `grid[0][2]` is 2 (non-negative).
   - Move to the next row: `row = 1`.
3. Now at `(1, 2)`. `grid[1][2]` is 1 (non-negative).
   - Move to the next row: `row = 2`.
4. Now at `(2, 2)`. `grid[2][2]` is -1 (negative).
   - All elements below it are also negative. There are `4 - 2 = 2` rows from here. So, `count = 4 + 2 = 6`.
   - Move to the previous column: `col = 1`.
5. Now at `(2, 1)`. `grid[2][1]` is 1 (non-negative).
   - Move to the next row: `row = 3`.
6. Now at `(3, 1)`. `grid[3][1]` is -1 (negative).
   - All elements below it are also negative. There is `4 - 3 = 1` row from here. So, `count = 6 + 1 = 7`.
   - Move to the previous column: `col = 0`.
7. Now at `(3, 0)`. `grid[3][0]` is -1 (negative).
   - All elements below it are also negative. There is `4 - 3 = 1` row from here. So, `count = 7 + 1 = 8`.
   - Move to the previous column: `col = -1`.
8. The loop terminates because `col` is out of bounds.
We return `count`, which is 8.

Time Complexity:
O(m + n), where m is the number of rows and n is the number of columns. In the worst case, we traverse through all the rows and columns once.

Space Complexity:
O(1), as we are not using any extra space.
'''