from collections import deque
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        sortedOrder = []
        if numCourses <= 0:
            return
        # intialize
        inDegree = {i:0 for i in range(numCourses)}
        graph = {i:[] for i in range(numCourses)}

        # populate graph
        for prereq in prerequisites:
            parent, child = prereq[0], prereq[1]
            graph[parent].append(child)
            inDegree[child] += 1
        
        # find all sources
        sources = deque()
        for key in inDegree:
            if inDegree[key] == 0:
                sources.append(key)

        # topo sort
        while sources:
            vertex = sources.popleft()
            sortedOrder.append(vertex)
            for child in graph[vertex]:
                inDegree[child] -= 1
                if inDegree[child] == 0:
                    sources.append(child)
                    
        if len(sortedOrder) != numCourses:
            return False
        return True
