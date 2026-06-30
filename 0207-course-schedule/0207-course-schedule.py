class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = {i:[] for i in range(numCourses)}
        indegree = [0] * numCourses

        for u, v in prerequisites:
            graph[u].append(v)
            indegree[v] += 1

        queue = deque()

        for node in range(numCourses):
            if indegree[node] == 0:
                queue.append(node)
        
        topo_order = []
        while queue:
            curr = queue.popleft()
            topo_order.append(curr)

            for ne in graph[curr]:
                indegree[ne] -= 1
                if indegree[ne] == 0:
                    queue.append(ne)
        
        return len(topo_order) == numCourses
