# Difficulty: Medium

# Brute Force Solution
#     def searchRange(self, nums: List[int], target: int) -> List[int]:
#         first = -1
#         last = -1
#         for i in range(len(nums)):
#             if nums[i] == target:
#                 if first == -1:
#                     first = i
#                 last = i
#         return [first, last]

# def searchRange(nums, target):
#     def findFirst(nums, target):
#       low, high = 0, len(nums) - 1
#       first = -1
#       while low <= high:
#         mid = (low + high) // 2
#         if nums[mid] >= target:
#           high = mid - 1
#         else:
#           low = mid + 1
#         if nums[mid] == target:
#           first = mid
#       return first

#     def findLast(nums, target):
#       low, high = 0, len(nums) - 1
#       last = -1
#       while low <= high:
#         mid = (low + high) // 2
#         if nums[mid] <= target:
#           low = mid + 1
#         else:
#           high = mid - 1
#         if nums[mid] == target:
#           last = mid
#       return last

#     first = findFirst(nums, target)
#     last = findLast(nums, target)

#     return [first, last]




'''
Intuition
The problem asks us to find the starting and ending positions of a given target value in a sorted array of integers. If the target is not found, we should return [-1, -1]. The solution must have a time complexity of O(log n), which suggests using a binary search algorithm.

A standard binary search can find an instance of the target, but it doesn't guarantee finding the first or last occurrence. To solve this, we can modify the binary search algorithm to find the first and last positions separately.

To find the first position, we perform a binary search but adjust the logic to continue searching in the left half of the array even after finding a target. This ensures we find the leftmost occurrence. Specifically, when `nums[mid] == target`, we store the index `mid` and then try to find an even earlier occurrence by setting `high = mid - 1`.

To find the last position, we perform another binary search. This time, when `nums[mid] == target`, we store the index `mid` and continue searching in the right half by setting `low = mid + 1`. This ensures we find the rightmost occurrence.

The overall approach is to run these two modified binary searches: one to find the first position and another to find the last position. If the first search doesn't find the target, we can immediately return `[-1, -1]`. Otherwise, we proceed with the second search and return the results.

Example Walkthrough
Let's walk through an example: `nums = [5, 7, 7, 8, 8, 10]` and `target = 8`.

Finding the first position of 8:
1. Initialize `low = 0`, `high = 5`, `first = -1`.
2. `mid = 2`, `nums[2] = 7`. Since `7 < 8`, we search the right half: `low = 3`.
3. `mid = 4`, `nums[4] = 8`. We found a target, so `first = 4`. We continue searching for an earlier occurrence: `high = 3`.
4. `mid = 3`, `nums[3] = 8`. We found another target, so `first = 3`. We continue searching: `high = 2`.
5. Now `low > high`, so the loop terminates. The first position is 3.

Finding the last position of 8:
1. Initialize `low = 0`, `high = 5`, `last = -1`.
2. `mid = 2`, `nums[2] = 7`. Since `7 < 8`, we search the right half: `low = 3`.
3. `mid = 4`, `nums[4] = 8`. We found a target, so `last = 4`. We continue searching for a later occurrence: `low = 5`.
4. `mid = 5`, `nums[5] = 10`. Since `10 > 8`, we search the left half: `high = 4`.
5. Now `low > high`, so the loop terminates. The last position is 4.

The result is `[3, 4]`.

Complexities
- Time Complexity: O(log n) because we perform two separate binary searches, each taking O(log n) time.
- Space Complexity: O(1) because we only use a few variables to store indices and do not use any extra space that scales with the input size.
'''
