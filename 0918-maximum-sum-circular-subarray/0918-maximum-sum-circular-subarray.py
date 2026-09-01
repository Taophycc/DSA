class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        global_min = global_max = nums[0]
        curr_max = curr_min = 0
        total = 0

        for num in nums:
            curr_max = max(curr_max + num, num)
            curr_min = min(curr_min + num, num)
            total += num

            global_max = max(curr_max, global_max)
            global_min = min(curr_min, global_min)

        return max(total - global_min, global_max) if global_max > 0 else global_max