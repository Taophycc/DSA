from collections import defaultdict
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        """
        Validates the initial state of a 9x9 Sudoku board.

        This method checks whether the board is valid according to the following 
        three Sudoku rules:
        1. Each row must contain the digits 1-9 without repetition.
        2. Each column must contain the digits 1-9 without repetition.
        3. Each of the nine 3x3 sub-boxes of the grid must contain the digits 1-9 without repetition.

        Note:
        - A valid board (partially filled) is not necessarily solvable. 
        - Only the filled cells need to be validated.

        Args:
            board (List[List[str]]): A 9x9 2D list containing strings. 
                                     Cells contain digits '1'-'9' or '.' for empty cells.

        Returns:
            bool: True if all filled cells satisfy the Sudoku rules, False otherwise.

        Algorithm:
            The solution iterates through the board once (single pass). It maintains 
            hash sets for every row, column, and 3x3 sub-box. For every non-empty 
            cell, it checks if the value already exists in the corresponding sets.
            
            - Row index: r
            - Column index: c
            - Square index: (r // 3, c // 3)

        Complexity Analysis:
            - Time Complexity: O(N^2) where N=9. Since the board size is fixed 
              at 9x9, this is technically O(1). We visit every cell exactly once.
            - Space Complexity: O(N^2) in the worst case to store the numbers 
              in the sets. Since the board is fixed, this is also O(1).
        """
        rows = defaultdict(set)
        cols = defaultdict(set)
        squares = defaultdict(set)

        for r in range(9):
            for c in range(9):
                if board[r][c] == '.':
                    continue
                if board[r][c] in rows[r] or board[r][c] in cols[c] or board[r][c] in squares[r//3,c//3]:
                    return False
                rows[r].add(board[r][c])    
                cols[c].add(board[r][c])    
                squares[r//3, c//3].add(board[r][c])    
        return True        
