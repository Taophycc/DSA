class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        n = len(nums)
        s = sorted(nums)
        current_streak = longest_streak = 1
        if not nums:
            return 0

        for i in range(len(s)-1):
            if s[i+1] == s[i] + 1:
                current_streak += 1
            elif s[i+1] == s[i]:
                continue
            else:
                longest_streak = max(current_streak, longest_streak)
                current_streak = 1
   
        return max(longest_streak, current_streak)
