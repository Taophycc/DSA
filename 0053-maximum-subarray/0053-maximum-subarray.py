class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_sub = nums[0]
        res = nums[0]

        for i in range(1, len(nums)):
            if max_sub < 0:
                max_sub = 0
            max_sub += nums[i]

            if max_sub > res:
                res = max_sub

        return res