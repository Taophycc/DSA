class Solution:
    def rob(self, nums: list[int]) -> int:
        cache = {}
        def rob_house(index):
            if index == 0: return nums[index]
            if index < 0: return 0

            if index in cache: return cache[index]

            pick = nums[index] + rob_house(index - 2)
            not_pick = 0 + rob_house(index-1)
            cache[index] = max(pick, not_pick)
            return max(pick, not_pick)

        return rob_house(len(nums)-1)