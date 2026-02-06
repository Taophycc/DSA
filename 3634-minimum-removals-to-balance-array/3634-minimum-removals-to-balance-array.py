class Solution:
    def minRemoval(self, nums: List[int], k: int) -> int:
        n = len(nums)
        cnt = 0
        nums.sort()
        max_kept = 0
        r = 0
        for l in range(n):
            while r < n and nums[r] <= nums[l] * k:
                r+=1
            curr_window = r - l
            max_kept = max(max_kept, curr_window)
        return n - max_kept