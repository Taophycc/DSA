class Solution:
    def missingInteger(self, nums: List[int]) -> int:
        n = len(nums)
        summ = nums[0]
        j = 1

        while j < n and nums[j] == nums[j-1] + 1:
            summ += nums[j]
            j += 1

        nums_set = set(nums)
        while summ in nums_set:
            summ += 1
        return summ