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
# # 1. **Finding the First Zero:** The code first scans the array to find the index of the very first zero. This index is stored in `j`. If no zero is found, the array is already sorted in the desired way, and the function returns.
# #
# # 2. **Swapping Elements:** After finding the first zero at index `j`, the code continues scanning from the next element (`i = j + 1`).
# #    - The pointer `j` now marks the position of the first available spot for a non-zero number (which currently holds a zero).
# #    - The pointer `i` scans ahead looking for the next non-zero number.
# #    - When `i` finds a non-zero number, it swaps its value with the value at `j`.
# #    - After the swap, `j` is incremented to point to the next position that needs to be filled with a non-zero number.
# #
# # This process ensures that all non-zero numbers are moved to the front of the array in their original relative order.
# #
# # **Example Walkthrough:** `nums = [0, 1, 0, 3, 12]`
# #
# # 1. **Find First Zero:** The first loop finds the first zero at index 0. So, `j = 0`.
# #
# # 2. **Start Swapping:** The second loop starts with `i = 1`.
# #    - **i = 1:** `nums[1]` is 1 (non-zero). Swap `nums[1]` with `nums[0]`.
# #        - `nums` becomes `[1, 0, 0, 3, 12]`.
# #        - `j` increments to 1.
# #
# #    - **i = 2:** `nums[2]` is 0. Nothing happens.
# #
# #    - **i = 3:** `nums[3]` is 3 (non-zero). Swap `nums[3]` with `nums[j]` (which is `nums[1]`).
# #        - `nums` becomes `[1, 3, 0, 0, 12]`.
# #        - `j` increments to 2.
# #
# #    - **i = 4:** `nums[4]` is 12 (non-zero). Swap `nums[4]` with `nums[j]` (which is `nums[2]`).
# #        - `nums` becomes `[1, 3, 12, 0, 0]`.
# #        - `j` increments to 3.
# #
# # The loop finishes.
# #
# # **Final Result:** `[1, 3, 12, 0, 0]`