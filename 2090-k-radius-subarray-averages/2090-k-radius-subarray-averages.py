class Solution:
    def getAverages(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        window_size = 2*k+1
        res = [-1] * n
        
        if n < window_size:
            return res
        
        window_sum = sum(nums[:window_size])
        res[k] = window_sum // window_size

        for i in range(k+1, n-k):
            window_sum = window_sum + nums[i+k] - nums[i-k-1] 
            res[i] = window_sum // window_size

        return res
