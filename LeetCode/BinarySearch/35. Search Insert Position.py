# Difficulty - EASY

# def searchInsert(nums, target):
#     low = 0
#     high = len(nums) - 1
#     ans = len(nums)

#     while low <= high:
#         mid = (low + high) // 2
#         if nums[mid] >= target:
#             ans = mid
#             high = mid -1
#         else:
#             low = mid + 1
#     return ans

# Intuition
# The problem asks for the index of a target value in a sorted array. If the target is not found, it asks for the index where it would be if it were inserted in order.
# This is a classic binary search problem. The key insight is to find the first element that is greater than or equal to the target.
# This position will be the target's index if it exists, or the insertion point if it doesn't.

# Walkthrough
# 1. Initialize `low` to 0 and `high` to the last index of the array.
# 2. Initialize `ans` to the length of the array. This will be the default insertion point if the target is greater than all elements.
# 3. While `low` is less than or equal to `high`:
#    a. Calculate the middle index `mid`.
#    b. If the element at `mid` is greater than or equal to the `target`, it means `mid` could be our answer. We store `mid` in `ans` and move our search to the left half (`high = mid - 1`) to see if we can find an even earlier position.
#    c. If the element at `mid` is less than the `target`, we need to look in the right half, so we update `low = mid + 1`.
# 4. After the loop, `ans` will hold the index of the first element that is greater than or equal to the target, which is the desired insertion position.

# Walkthrough Example
# nums = [1, 3, 5, 6], target = 5
# 1. low = 0, high = 3, ans = 4. mid = 1. nums[1] (3) < 5. low becomes 2.
# 2. low = 2, high = 3, ans = 4. mid = 2. nums[2] (5) >= 5. ans becomes 2, high becomes 1. Loop terminates as low > high.
# 3. Return ans which is 2.

# Time Complexity: O(log n)
# Binary search reduces the search space by half in each iteration.

# Space Complexity: O(1)
# We are only using a few variables to keep track of indices, so the space used is constant.
