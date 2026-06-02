from collections import deque
class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        visited = [False] * n
        queue = deque()
        graph = {i:[] for i in range(n)}
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
        queue.append(source)

        while queue:
            current = queue.popleft()
            if current == destination:
                return True

            for neighbor in graph[current]:
                if not visited[neighbor]:
                    visited[neighbor] = True
                    queue.append(neighbor)
        return False


