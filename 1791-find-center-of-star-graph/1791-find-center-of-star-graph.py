class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        seen = set()
        
        for i in range(2):
            u, v = edges[i][0], edges[i][1]
            
            if u in seen:
                return u
            if v in seen:
                return v
                
            seen.add(u)
            seen.add(v)
            
        return -1