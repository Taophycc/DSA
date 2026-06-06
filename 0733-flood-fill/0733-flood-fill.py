class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        if image[sr][sc] == color:
            return image
        n, m = len(image), len(image[0])
        visited = set()
        originalColour = image[sr][sc]

        def dfs(r, c):
            visited.add((r,c))
            image[r][c] = color

            directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
            for dr, dc in directions:
                neigh_r, neigh_c = r + dr, c + dc

                if (0 <= neigh_r < n) and (0 <= neigh_c < m):
                    if (neigh_r, neigh_c) not in visited and image[neigh_r][neigh_c] == originalColour:
                            dfs(neigh_r, neigh_c)
        dfs(sr, sc)
        return image