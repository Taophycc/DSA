class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)
        longest = 0

        for num in numSet:
            if (num-1) not in numSet:
                cnt = 1
                while (num + cnt) in numSet:
                    cnt += 1
                longest = max(longest, cnt)
        return longest
