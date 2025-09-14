# Difficulty - MEDIUM

# def rotate(self, nums: List[int], k: int) -> None:
#         """
#         Do not return anything, modify nums in-place instead.
#         """
#         n = len(nums)
#         k = k % n 
#         cnt = 0  

#         for i in range(n):
#             if cnt >= n:  
#                 break

#             current = i
#             temp = nums[i]

#             while True:
#                 next_index = (current + k) % n
#                 nums[next_index], temp = temp, nums[next_index]
#                 current = next_index
#                 cnt += 1

#                 if i == current: 
#                     break

# # --- EXPLANATION ---
# #
# # **Technique: Cyclic Replacements (Juggling Algorithm)**
# #
# # The intuition is to move elements in cycles. An element at index `i` is moved to `(i + k) % n`.
# # The key is the swap: `nums[next_index], temp = temp, nums[next_index]`. The `temp` variable holds
# # the element that was just displaced, which is then carried to its new position in the next iteration.
# # This continues until we loop back to the starting index `i`.
# #
# # An outer loop and a `cnt` counter are used to handle cases where multiple (disjoint) cycles
# # are needed to move all the elements.
# #
# # **Detailed Walkthrough:** `nums = [1, 2, 3, 4, 5, 6]`, `k = 2`
# #
# # **Cycle 1 (starts at i=0):**
# #    - `temp` is set to `nums[0]`, so `temp = 1`.
# #    - **Step 1:** `next_index` is 2. Swap `temp` (1) with `nums[2]` (3).
# #        - `nums` becomes `[1, 2, 1, 4, 5, 6]`.
# #        - `temp` becomes `3`.
# #    - **Step 2:** `next_index` is 4. Swap `temp` (3) with `nums[4]` (5).
# #        - `nums` becomes `[1, 2, 1, 4, 3, 6]`.
# #        - `temp` becomes `5`.
# #    - **Step 3:** `next_index` is 0. Swap `temp` (5) with `nums[0]` (1).
# #        - `nums` becomes `[5, 2, 1, 4, 3, 6]`.
# #        - `temp` becomes `1`.
# #    - Cycle 1 ends as we are back at index 0.
# #
# # **Cycle 2 (starts at i=1, with `nums = [5, 2, 1, 4, 3, 6]`):**
# #    - `temp` is set to `nums[1]`, so `temp = 2`.
# #    - **Step 1:** `next_index` is 3. Swap `temp` (2) with `nums[3]` (4).
# #        - `nums` becomes `[5, 2, 1, 2, 3, 6]`.
# #        - `temp` becomes `4`.
# #    - **Step 2:** `next_index` is 5. Swap `temp` (4) with `nums[5]` (6).
# #        - `nums` becomes `[5, 2, 1, 2, 3, 4]`.
# #        - `temp` becomes `6`.
# #    - **Step 3:** `next_index` is 1. Swap `temp` (6) with `nums[1]` (2).
# #        - `nums` becomes `[5, 6, 1, 2, 3, 4]`.
# #        - `temp` becomes `2`.
# #    - Cycle 2 ends as we are back at index 1.
# #
# # **Final Result:** `nums = [5, 6, 1, 2, 3, 4]`