class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        #Choice: Pick a number at index i to add to the path.
        #Constraints: Skip if index i is already used OR if it's an identical twin of the previous number (nums[i] == nums[i-1]) and we are starting a new branch.
        #Goal: Path length equals input length.

        n = len(nums)
        res = []
        path = []
        visited = set()

        nums.sort()

        def backtrack():
            if len(path) == len(nums):
                res.append(path[:])
                return
            
            for i in range(n):
                if i in visited:
                    continue 
                
                if i > 0 and nums[i] == nums[i-1] and (i-1) not in visited:
                    continue
                path.append(nums[i])
                visited.add(i)
                backtrack()
                path.pop()
                visited.remove(i)
                    
        backtrack()
        return res