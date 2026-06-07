class Solution:
    def leftRightDifference(self, nums: List[int]) -> List[int]:
        n = len(nums)
        leftSum = [0] * n
        leftSum[0] = 0
        rightSum = [0] * n
        ans= [0] * n
        for i in range(1, n):
            leftSum[i] = nums[i-1] + leftSum[i-1]

        for i in range(n-2, -1, -1):
            rightSum[i] = nums[i+1] + rightSum[i+1]

        for i in range(n):
            ans[i] = abs(leftSum[i] - rightSum[i])

        return ans