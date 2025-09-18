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
# # This approach leverages a classic mathematical formula to find the missing number. The idea is based on the sum of an arithmetic series.
# #
# # 1. **Calculate the Expected Sum:** The list `nums` contains `n` numbers, and it is missing one number from the range `[0, n]`. If the list were complete, it would contain `n+1` numbers from `0` to `n`. The sum of such a sequence can be calculated instantly using the formula `n * (n + 1) / 2`. This is the `expectedSum`.
# #
# # 2. **Calculate the Actual Sum:** The code then calculates the sum of the numbers that are actually present in the input list `nums`. This is the `actualSum`.
# #
# # 3. **Find the Difference:** The missing number is simply the difference between the `expectedSum` and the `actualSum`. The value that was "left out" is the one that accounts for this difference.
# #
# # This method is very efficient as it requires only a single pass to calculate the `actualSum`, and the `expectedSum` is calculated in constant time.
# #
# # **Example Walkthrough:** `nums = [3, 0, 1]`
# #
# # 1. **`n`:** The length of `nums` is 3.
# #
# # 2. **`expectedSum`:** The list should contain numbers from the range `[0, 3]`. The expected sum is `3 * (3 + 1) / 2 = 6`.
# #    (i.e., 0 + 1 + 2 + 3 = 6)
# #
# # 3. **`actualSum`:** The sum of the elements in the given `nums` is `3 + 0 + 1 = 4`.
# #
# # 4. **Difference:** The missing number is `expectedSum - actualSum` = `6 - 4 = 2`.
# #
# # **Final Result:** 2.