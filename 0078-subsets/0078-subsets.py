class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        sub = []
        res = []

        def backtrack(k):
            if k == len(nums):
                res.append(sub[:])
                return
            else:
                backtrack(k+1)
                sub.append(nums[k])
                backtrack(k+1)
                sub.pop()
        backtrack(0)
        return res