# Difficulty - EASY

# def sumBase(self, n: int, k: int) -> int:
#     digit_sum = 0
#     while n > 0:
#         digit_sum += n % k
#         n //= k
#     return digit_sum

#############
# Explanation
#############

# Intuition
# The problem asks for the sum of the digits of a number `n` after it has been converted from base-10 to base `k`. The standard algorithm for converting a number to a different base is to repeatedly take the number modulo `k` to get the next digit, and then integer divide the number by `k` to prepare for the next iteration. We can sum these digits as we find them.

# Walkthrough
# 1. Initialize a variable, `digit_sum`, to 0. This will store the sum of the digits in base `k`.
# 2. Start a loop that continues as long as the number `n` is greater than 0.
# 3. Inside the loop, calculate the remainder of `n` divided by `k` (`n % k`). This remainder is the rightmost digit of `n` in base `k`.
# 4. Add this digit to `digit_sum`.
# 5. Update `n` by integer dividing it by `k` (`n //= k`). This effectively removes the last digit in base `k`, preparing for the next digit extraction.
# 6. The loop continues until `n` becomes 0, at which point all digits have been extracted and summed.
# 7. Return `digit_sum`.

# Walkthrough Example
# n = 34, k = 6
# (34 in base-10 is equivalent to 54 in base-6. The sum of digits is 5 + 4 = 9)
# 1. Initialize `digit_sum = 0`.
# 2. **Loop 1:**
#    - `n = 34`. `n > 0` is true.
#    - `remainder = 34 % 6 = 4`.
#    - `digit_sum = 0 + 4 = 4`.
#    - `n = 34 // 6 = 5`.
# 3. **Loop 2:**
#    - `n = 5`. `n > 0` is true.
#    - `remainder = 5 % 6 = 5`.
#    - `digit_sum = 4 + 5 = 9`.
#    - `n = 5 // 6 = 0`.
# 4. **Loop 3:**
#    - `n = 0`. `n > 0` is false. The loop terminates.
# 5. Return `digit_sum`, which is 9.

# Time Complexity: O(log_k(n))
# The number of times we can divide `n` by `k` before it becomes 0 is given by the logarithm of `n` to the base `k`.

# Space Complexity: O(1)
# We only use a few variables to store the sum and the intermediate results. The space required is constant and does not depend on the size of the input `n`.