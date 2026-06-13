class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        n = len(rooms)
        visited = set()

        def dfs(curr):
            visited.add(curr)

            for key in rooms[curr]:
                if key not in visited:
                    dfs(key)
            
        dfs(0)
        return len(visited) == len(rooms)