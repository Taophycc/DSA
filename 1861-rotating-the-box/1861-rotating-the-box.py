from collections import deque
class Solution:
    def rotateTheBox(self, boxGrid: List[List[str]]) -> List[List[str]]:
        rows, cols = len(boxGrid), len(boxGrid[0])

        for r in range(rows):
            empty_slot = cols - 1
            for c in range(cols-1,-1, -1):
                if boxGrid[r][c] == "#":
                    boxGrid[r][c], boxGrid[r][empty_slot] = boxGrid[r][empty_slot], boxGrid[r][c]
                    empty_slot -= 1
                elif boxGrid[r][c] == "*":
                    empty_slot = c - 1

        rotatedBox = [[None]*rows for _ in range(cols)]
        for row in range(rows):
            for col in range(cols):
                rotatedBox[col][rows - 1 - row] = boxGrid[row][col]
        return rotatedBox
