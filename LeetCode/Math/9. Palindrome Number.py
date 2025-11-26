# Difficulty - EASY

# def isPalindrome(x):
#         if x < 0 or (x % 10 == 0 and x != 0):
#             return False

#         reversed_num = 0
#         original = x

#         while x > 0:
#             digit = x % 10

#             reversed_num = (reversed_num * 10) + digit
#             x //= 10
            
#         return original == reversed_num

#############
# Explanation
#############

# Intuition
# A number is a palindrome if it reads the same forwards and backward. The most direct way to check this is to reverse the number and then compare the reversed version to the original. If they are identical, it's a palindrome.
# We should also handle edge cases first:
# 1. Negative numbers are not palindromes (e.g., the reverse of -121 is 121-).
# 2. Numbers ending in 0 (that are not 0 itself) cannot be palindromes because the reversed number would not have a leading zero (e.g., 120 reversed is 21).

# Walkthrough
# 1. First, handle the edge cases. If the input `x` is negative, or if it ends in a 0 but is not 0 itself, return `False` immediately.
# 2. Store the original value of `x` in a separate variable, `original`, so we don't lose it.
# 3. Initialize a variable `reversed_num` to 0. This will be used to build the reversed number.
# 4. Start a loop that continues as long as `x` is greater than 0.
# 5. Inside the loop, get the last digit of `x` using the modulo operator (`digit = x % 10`).
# 6. Append this digit to `reversed_num`. This is done by multiplying `reversed_num` by 10 and adding the `digit`.
# 7. Remove the last digit from `x` using integer division (`x //= 10`).
# 8. Once the loop finishes, `x` will be 0, and `reversed_num` will hold the complete reversed number.
# 9. Compare `original` with `reversed_num`. If they are equal, the number is a palindrome, so return `True`. Otherwise, return `False`.

# Walkthrough Example
# x = 121
# 1. `x` is not negative and doesn't end in 0. `original = 121`, `reversed_num = 0`.
# 2. **Loop 1:** `digit = 121 % 10 = 1`. `reversed_num = (0 * 10) + 1 = 1`. `x = 121 // 10 = 12`.
# 3. **Loop 2:** `digit = 12 % 10 = 2`. `reversed_num = (1 * 10) + 2 = 12`. `x = 12 // 10 = 1`.
# 4. **Loop 3:** `digit = 1 % 10 = 1`. `reversed_num = (12 * 10) + 1 = 121`. `x = 1 // 10 = 0`.
# 5. Loop terminates because `x` is now 0.
# 6. Compare `original` (121) with `reversed_num` (121). They are equal. Return `True`.

# Time Complexity: O(log10(n))
# The time taken is proportional to the number of digits in the input number `n`. The number of digits is given by log10(n).

# Space Complexity: O(1)
# We only use a few variables to store the original number, the reversed number, and the current digit. The space is constant and does not depend on the input size.