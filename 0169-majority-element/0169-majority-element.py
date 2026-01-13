class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        nums.sort()
        n = len(nums)
        l = 0
        r = n-1

        mid = (l+r)//2
        return nums[mid]