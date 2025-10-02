# DIfficulty - EASY

# Iterative method
# def binarySearch(nums, target):
#     low = 0
#     high = len(nums) - 1

#     while low <= high:
#         mid = (high+low) // 2

#         if nums[mid] == target:
#             return mid
#         elif nums[mid] > target:
#             high = mid - 1
#         else:
#             low = mid + 1
#     return -1

# Recursive method
# def binarySearchRecursive(nums, low, high, target):
#     if low > high:
#         return -1

#     mid = (high+low) // 2

#     if nums[mid] == target:
#         return mid
#     elif nums[mid] > target:
#         return binarySearchRecursive(nums, low, mid - 1, target)
#     else:
#         return binarySearchRecursive(nums, mid + 1, high, target)


# Intuition
# Binary search is an efficient algorithm for finding an item from a sorted list of items. It works by repeatedly dividing in half the portion of the list that could contain the item, until you've narrowed down the possible locations to just one.

# Walkthrough (Iterative)
# 1. Initialize `low` to 0 and `high` to the last index of the array.
# 2. While `low` is less than or equal to `high`:
#    a. Calculate the middle index `mid`.
#    b. If the element at `mid` is the `target`, return `mid`.
#    c. If the element at `mid` is greater than the `target`, it means the target must be in the left half, so we update `high = mid - 1`.
#    d. If the element at `mid` is less than the `target`, it means the target must be in the right half, so we update `low = mid + 1`.
# 3. If the loop finishes without finding the target, it means the target is not in the array, so we return -1.

# Walkthrough Example (Iterative)
# nums = [-1, 0, 3, 5, 9, 12], target = 9
# 1. low = 0, high = 5. mid = 2. nums[2] (3) < 9. low becomes 3.
# 2. low = 3, high = 5. mid = 4. nums[4] (9) == 9. Return 4.

# Time Complexity: O(log n)
# Binary search reduces the search space by half in each iteration.

# Space Complexity (Iterative): O(1)
# We are only using a few variables to keep track of indices, so the space used is constant.

# Space Complexity (Recursive): O(log n)
# The space complexity of the recursive version is O(log n) because of the recursion stack. In each recursive call, a new frame is pushed onto the stack. The maximum depth of the recursion is log n.
