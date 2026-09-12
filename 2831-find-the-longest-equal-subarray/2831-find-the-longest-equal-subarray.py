class Solution:
    def longestEqualSubarray(self, nums: List[int], k: int) -> int:
        n = len(nums)
        mp = defaultdict(int)
        l = 0
        max_freq = 0

        for r in range( n):
            mp[nums[r]] += 1
            max_freq = max(max_freq, mp[nums[r]])

            window_len = r-l+1
            if window_len - max_freq > k:
                mp[nums[l]] -= 1
                l += 1

        return max_freq