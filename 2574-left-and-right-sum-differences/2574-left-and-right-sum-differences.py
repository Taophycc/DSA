class Solution:
    def leftRightDifference(self, nums: List[int]) -> List[int]:
        n = len(nums)
        ans= [0] * n

        leftSum = 0
        for i in range(n):
            ans[i] = leftSum
            leftSum += nums[i]

        rightSum = 0
        for i in range(n-1, -1, -1):
            ans[i] = abs(ans[i] - rightSum)
            rightSum += nums[i]

        return ans