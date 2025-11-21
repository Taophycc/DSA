# Difficulty - EASY

# def findFinalValue(self, nums: List[int], original: int) -> int:
#         nums_set = set(nums)

#         while original in nums_set:
#             original = 2 * original

#         return original

###############
# Optimal
###############

# Intuition
# The problem requires us to check for the existence of a number in an array repeatedly.
# To make these checks efficient, we can convert the input array `nums` into a hash set.
# A hash set provides average O(1) time complexity for lookups.

# Walkthrough
# 1. Create a hash set `nums_set` from the input list `nums`. This allows for quick checking of whether a number exists.
# 2. Start a `while` loop that continues as long as the current `original` value is found in `nums_set`.
# 3. Inside the loop, if `original` is present in the set, we update `original` by multiplying it by 2.
# 4. The loop will exit when the (potentially updated) `original` value is no longer in `nums_set`.
# 5. Finally, we return the last `original` value.

# Walkthrough Example
# nums = [5, 3, 6, 1, 12], original = 3
# 1. Create nums_set: {1, 3, 5, 6, 12}.
# 2. `original` is 3. Is 3 in the set? Yes. Update original to 3 * 2 = 6.
# 3. `original` is 6. Is 6 in the set? Yes. Update original to 6 * 2 = 12.
# 4. `original` is 12. Is 12 in the set? Yes. Update original to 12 * 2 = 24.
# 5. `original` is 24. Is 24 in the set? No. The loop terminates.
# 6. Return the final `original` value, which is 24.

# Time Complexity: O(n)
# The initial conversion of the list `nums` to a set takes O(n) time, where n is the number of elements in `nums`.
# The `while` loop's execution time depends on the number of times we can double `original` before it's not in the set. In the worst case, this is bounded. The dominant factor is the set creation.

# Space Complexity: O(n)
# We use a hash set to store all the elements from the input array, which requires O(n) extra space.
