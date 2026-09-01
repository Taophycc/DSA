class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_sub = nums[0]
        res = nums[0]

        for i in range(1, len(nums)):
            max_sub = max(max_sub + nums[i], nums[i])

            res = max(res, max_sub)
        return res