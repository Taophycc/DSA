# DIfficulty - EASY

# def missingNumber(nums):
#     n = len(nums)
#     expectedSUm = n * (n + 1)//2
#     actualSum = sum(nums)
#     return expectedSUm - actualSum

# # --- EXPLANATION ---
# #
# # **Intuition: Summation Formula (Gauss's Law)**
# #
# # This approach leverages a classic mathematical formula. The idea is to compare the expected sum of the sequence `[0, n]` with the actual sum of the numbers in the list.
# #
# # 1. **Expected Sum:** The sum of a sequence of numbers from 0 to `n` is calculated with the formula `n * (n + 1) / 2`.
# # 2. **Actual Sum:** The code calculates the sum of the numbers provided in the input list.
# # 3. **Difference:** The missing number is the difference between the `expectedSum` and the `actualSum`.
# #
# # **Complexity:**
# # - Time: O(n), because the `sum()` function iterates through the entire list once.
# # - Space: O(1), as the storage required is constant.
# #
# # **Example Walkthrough:** `nums = [3, 0, 1]`
# #
# # 1. **`n`:** The length of `nums` is 3.
# # 2. **`expectedSum`:** `3 * (3 + 1) / 2 = 6`.
# # 3. **`actualSum`:** `3 + 0 + 1 = 4`.
# # 4. **Difference:** `6 - 4 = 2`.
# #
# # **Final Result:** 2.
