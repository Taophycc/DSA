# Difficulty - EASY

#   def moveZeroes(self, nums: List[int]) -> None:
#         """
#         Do not return anything, modify nums in-place instead.
#         """
#         n = len(nums)
#         j = -1

#         for i in range(n):
#             if nums[i] == 0:
#                 j = i
#                 break

#         if j == -1:
#             return 

#         m = j+1
#         for i in range(m, n):
#             if nums[i] != 0:    
#                 nums[i], nums[j] = nums[j], nums[i]
#                 j += 1

# # --- EXPLANATION ---
# #
# # **Intuition: Two-Pointer Approach**
# #
# # This solution uses a two-pointer technique to move all non-zero elements to the front of the array in a single pass, effectively pushing all zeroes to the end.
# #
# # 1. **Finding the First Zero:** The code first finds the index of the first zero (`j`). If none exists, the operation is complete.
# #
# # 2. **Swapping Elements:** It then uses a second pointer (`i`) to scan for non-zero elements.
# #    - When `i` finds a non-zero number, it swaps it with the zero at `j`.
# #    - `j` is then incremented to point to the next zero, maintaining the relative order of non-zero elements.
# #
# # **Complexity:**
# # - Time: O(n), because each element is visited a constant number of times.
# # - Space: O(1), as the swaps are done in-place.
# #
# # **Example Walkthrough:** `nums = [0, 1, 0, 3, 12]`
# #
# # 1. **Find First Zero:** First loop finds a zero at index 0. `j` becomes 0.
# #
# # 2. **Start Swapping:** Second loop starts at `i = 1`.
# #    - **i = 1:** `nums[1]` is 1. Swap `nums[1]` and `nums[0]`. `nums` -> `[1, 0, 0, 3, 12]`. `j` increments to 1.
# #    - **i = 2:** `nums[2]` is 0. Nothing happens.
# #    - **i = 3:** `nums[3]` is 3. Swap `nums[3]` and `nums[1]`. `nums` -> `[1, 3, 0, 0, 12]`. `j` increments to 2.
# #    - **i = 4:** `nums[4]` is 12. Swap `nums[4]` and `nums[2]`. `nums` -> `[1, 3, 12, 0, 0]`. `j` increments to 3.
# #
# # **Final Result:** `[1, 3, 12, 0, 0]`
