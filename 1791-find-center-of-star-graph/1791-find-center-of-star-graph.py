class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        ans = set()
        
        for i in range(2):
            if edges[i][0] in ans:
                return edges[i][0]
            elif edges[i][1] in ans:
                return edges[i][1]
            ans.add(edges[i][0])
            ans.add(edges[i][1])
        return ans