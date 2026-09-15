class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        # atleat 3 sides
        # lomgest side is smaller than the sum of other sides
        # in nums the longest side could only be in icluded in the polygon if there exits a sum of other sides greater than it

        # 1,12,1,2,5,50,3
        #1,1,2,3,5,12, 50

        # 5,5,50

        # 1,1,2,3,5,12,50 - {1,1,2,3 = 7, 12}
        # curr_sum += nums[0] + nums[1]
        # for i in range(2, n):
            # curr_sum += nums[i]
        #   if nums[i] < curr_sum:
            # perimeter = curr_sum + nums[i]
        n = len(nums)
        nums.sort()
        curr_sum = nums[0] + nums[1]
        perimeter = 0
        for i in range(2, n):

            if nums[i] < curr_sum:
                perimeter = max(perimeter, curr_sum + nums[i])
            curr_sum += nums[i]
        return -1 if perimeter == 0 else perimeter