from collections import Counter
class Solution:
    def duplicateNumbersXOR(self, nums: List[int]) -> int:
        count = Counter(nums)
        res = 0
        for num, freq in count.items():
            if freq == 2:
                res ^= num
        return res
                