# Difficulty - EASY

# def check(self, nums: List[int]) -> bool:
#     c = 0
#     n = len(nums)
#     for i in range(n):
#         if nums[i] > nums[(i + 1) % len(nums)]:
#             c += 1
#             if c > 1:
#                 return False
#     return True

# # --- EXPLANATION ---
# #
# # **Intuition: Counting Rotational "Breaks"**
# #
# # A sorted array that has been rotated will have at most one "break" point where an element is larger than the element that follows it (in a circular sense). This code counts those breaks.
# #
# # The code iterates through the array, comparing each element `nums[i]` with the next, using the modulo operator `%` to handle the wrap-around from the last element to the first.
# #
# # If the number of breaks found is more than one, it's not a valid sorted-and-rotated array. A count of 0 (already sorted) or 1 (rotated) is valid.
# #
# # **Complexity:**
# # - Time: O(n), for the single pass through the array.
# # - Space: O(1), as only a counter variable is used.
# #
# # **Example: `nums = [3, 4, 5, 1, 2]`**
# #
# # 1. `c` starts at 0.
# # 2. The code finds a break at `i=2` where `nums[2]` (5) > `nums[3]` (1). `c` becomes 1.
# # 3. The loop continues, but no more breaks are found.
# # 4. The loop finishes, `c` is 1, so the function returns `True`.
