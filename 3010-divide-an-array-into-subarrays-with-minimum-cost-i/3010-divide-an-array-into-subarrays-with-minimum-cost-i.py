class Solution:
    def minimumCost(self, nums: List[int]) -> int:
        a = nums[0]
        b = float('inf')
        c = float('inf')

        for num in nums[1:]:
            if num < b:
                c = b
                b = num
            elif num < c:
                c = num
        return a + b + c