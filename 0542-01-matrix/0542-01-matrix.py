class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        from collections import deque
        rows, cols = len(mat),len(mat[0])
        dist = [[0]*cols for i in range(rows)]


        visited = set()
        queue = deque()

        for r in range(rows):
            for c in range(cols):
                if mat[r][c] == 0:
                    queue.append((r, c))
                    visited.add((r,c))

        directions = [(1, 0), (-1,0), (0,1), (0,-1)]
        while queue:
            for _ in range(len(queue)):
                r, c = queue.popleft()

                for dr, dc in directions:
                    neigh_r, neigh_c = r + dr, c + dc

                    if (0 <= neigh_r < rows) and (0 <= neigh_c < cols):
                        if (neigh_r, neigh_c) not in visited:
                            dist[neigh_r][neigh_c] = dist[r][c] + 1
                            queue.append((neigh_r, neigh_c)) 
                            visited.add((neigh_r,neigh_c))

        return dist