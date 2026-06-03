class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)
        visited = [False] * n
        provinces = 0

        def dfs(current_city):
            visited[current_city] = True
            
            for neighbor in range(n):
                if isConnected[current_city][neighbor] == 1 and not visited[neighbor]:
                    dfs(neighbor)

        for i in range(n):
            if not visited[i]:
                provinces += 1
                dfs(i)
                
        return provinces