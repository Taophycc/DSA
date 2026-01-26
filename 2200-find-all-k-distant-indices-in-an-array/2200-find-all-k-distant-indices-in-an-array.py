class Solution:
    def findKDistantIndices(self, nums: List[int], key: int, k: int) -> List[int]:
        n = len(nums)
        res = []
        last_added = -1 

        for j in range(n):
            if nums[j] == key:
                start = j - k
                end = j + k
                
                start = max(0, start, last_added + 1)
                
                actual_end = min(n - 1, end)
                
                for i in range(start, actual_end + 1):
                    res.append(i)
                    last_added = i 
                    
        return res
