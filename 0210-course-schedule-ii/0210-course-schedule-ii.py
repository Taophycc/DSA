class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph = {i:[] for i in range(numCourses)}
        inDegree = [0] * numCourses
        topo_sorts = []
        queue = deque()
        
        for u, v in prerequisites:
            graph[v].append(u)
            inDegree[u] += 1 

        for i in range(numCourses):
            if inDegree[i] == 0:
                queue.append(i)

        while queue:
            node = queue.popleft()
            topo_sorts.append(node)

            for ne in graph[node]:
                inDegree[ne] -= 1
                if inDegree[ne] == 0:
                    queue.append(ne)

        return topo_sorts if len(topo_sorts) == numCourses else []
