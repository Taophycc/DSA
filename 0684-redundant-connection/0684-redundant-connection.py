from collections import deque

class Solution:
    def findRedundantConnection(self, edges: list[list[int]]) -> list[int]:
        n = len(edges)
        graph = {i: [] for i in range(1, n + 1)}

        def path_exists(source, target):
            queue = deque([source])
            visited = {source}

            while queue:
                curr = queue.popleft()
                if curr == target:
                    return True
                
                for neighbor in graph[curr]:
                    if neighbor not in visited:
                        visited.add(neighbor)
                        queue.append(neighbor)
            return False

        for u, v in edges:
            if path_exists(u, v):
                return [u, v]
            
            graph[u].append(v)
            graph[v].append(u)