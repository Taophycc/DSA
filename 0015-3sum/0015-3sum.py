from collections import defaultdict
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i-1]:
                continue

            target = -nums[i]

            l ,r = i + 1, len(nums) - 1
            while l < r:
                curr_sum = nums[l] + nums[r]

                if curr_sum == target:
                    res.append([nums[i], nums[l], nums[r]])

                    while l < r and nums[l] == nums[l+1]:
                        l+=1
                    while l< r and nums[r] == nums[r-1]:
                        r-=1
                    l += 1
                    r -= 1
                elif curr_sum < target:
                    l+=1
                else:
                    r-=1
        return res