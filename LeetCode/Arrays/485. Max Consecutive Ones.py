# Difficulty - EASY

# def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
#         n = len(nums)
#         count = max_count = 0

#         for num in nums:
#             if num == 1:
#                 count += 1
#                 max_count = max(count, max_count)
#             else:
#                 count = 0

#         return max_count

# # --- EXPLANATION ---
# #
# # **Technique: Single-Pass Iteration with a Counter**
# #
# # The intuition behind this code is to solve the problem in a single pass through the array, which is very efficient (O(n) time complexity).
# #
# # We use two variables:
# # 1. `count`: This tracks the number of consecutive ones in the *current* sequence we are looking at.
# # 2. `max_count`: This stores the highest `count` we have seen so far across all sequences.
# #
# # We iterate through each number in the input list `nums`:
# # - If the number is `1`, it means the current sequence of ones is continuing. We increment `count`.
# #   Then, we compare the `count` of the current sequence with our overall `max_count` and update `max_count` if the current one is longer.
# # - If the number is `0`, it means the sequence of ones is broken. We reset `count` back to `0`.
# #
# # By the end of the loop, `max_count` will hold the length of the longest sequence of consecutive ones found in the array.
# #
# # **Example Walkthrough:** `nums = [1, 1, 0, 1, 1, 1]`
# #
# # Initial state: `count = 0`, `max_count = 0`
# #
# # 1. **num = 1:**
# #    - `count` becomes 1.
# #    - `max_count` becomes `max(1, 0)` which is 1.
# #
# # 2. **num = 1:**
# #    - `count` becomes 2.
# #    - `max_count` becomes `max(2, 1)` which is 2.
# #
# # 3. **num = 0:**
# #    - The sequence is broken.
# #    - `count` is reset to 0.
# #
# # 4. **num = 1:**
# #    - `count` becomes 1.
# #    - `max_count` remains 2 (`max(1, 2)`).
# #
# # 5. **num = 1:**
# #    - `count` becomes 2.
# #    - `max_count` remains 2 (`max(2, 2)`).
# #
# # 6. **num = 1:**
# #    - `count` becomes 3.
# #    - `max_count` becomes `max(3, 2)` which is 3.
# #
# # The loop finishes.
# #
# # **Final Result:** `max_count` is returned, which is 3.