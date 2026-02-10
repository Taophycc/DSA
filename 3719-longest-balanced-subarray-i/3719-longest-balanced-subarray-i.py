class Solution:
    def longestBalanced(self, nums: List[int]) -> int:
        n = len(nums)
        max_len = 0

        for i in range(n):
            odds = set()
            evens = set()

            for j in range(i,n):
                num = nums[j]

                if num % 2 == 1:
                    odds.add(num)
                else:
                    evens.add(num)

                if len(odds) == len(evens):
                    max_len = max(max_len, j - i + 1)
        return max_len