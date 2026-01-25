class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        # input = [2,5,5,11]
        
        for i in range(n): # i = 1
            for j in range(i+1,n): # j = 
                if nums[i] + nums[j] == target:
                    return [i, j]
        return []

