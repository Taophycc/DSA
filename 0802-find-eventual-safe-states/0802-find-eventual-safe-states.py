class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        n = len(graph)
        has_cycle = {}
        path_visited = set()

        def dfs(curr):
            if curr in has_cycle:
                return has_cycle[curr]
            
            if curr in path_visited:
                return True

            path_visited.add(curr)

            for ne in graph[curr]:
                if dfs(ne):
                    has_cycle[ne] = True
                    path_visited.remove(curr)
                    return True
        
            path_visited.remove(curr)
            has_cycle[curr] = False
            return False

        safe_nodes = []
        for i in range(n):
            if not dfs(i):
                safe_nodes.append(i)
        return safe_nodes