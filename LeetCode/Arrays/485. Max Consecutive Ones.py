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
# # The intuition behind this code is to solve the problem in a single pass through the array.
# #
# # We use two variables:
# # 1. `count`: This tracks the number of consecutive ones in the *current* sequence.
# # 2. `max_count`: This stores the highest `count` we have seen so far.
# #
# # We iterate through each number in the input list `nums`:
# # - If the number is `1`, we increment `count` and update `max_count` if the current count is larger.
# # - If the number is `0`, the sequence of ones is broken, so we reset `count` back to `0`.
# #
# # **Complexity:**
# # - Time: O(n), as we iterate through the array once.
# # - Space: O(1), as we only use a few variables for storage.
# #
# # **Example Walkthrough:** `nums = [1, 1, 0, 1, 1, 1]`
# #
# # Initial state: `count = 0`, `max_count = 0`
# #
# # 1. **num = 1:** `count` becomes 1, `max_count` becomes 1.
# # 2. **num = 1:** `count` becomes 2, `max_count` becomes 2.
# # 3. **num = 0:** `count` is reset to 0.
# # 4. **num = 1:** `count` becomes 1. `max_count` is still 2.
# # 5. **num = 1:** `count` becomes 2. `max_count` is still 2.
# # 6. **num = 1:** `count` becomes 3, `max_count` becomes 3.
# #
# # **Final Result:** 3.
