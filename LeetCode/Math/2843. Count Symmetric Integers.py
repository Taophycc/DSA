# Difficulty - EASY

# def countSymmetricIntegers(self, low: int, high: int) -> int:
#     cnt = 0

#     for num in range(low, high+1):
#         s = str(num)
#         n = len(s)
        
#         # check if number of digits is odd
#         if n % 2 != 0:
#             continue

#         # find the middle of the digit
#         mid = n // 2    

#         # get the left and right digits
#         left = s[:mid]   
#         right = s[mid:] 

#         # calculate their individual sum
#         left_sum = sum(int(char) for char in left)
#         right_sum = sum(int(char) for char in right)

#         # if same, it is symmetric. increase cnt by 1
#         if left_sum == right_sum:
#             cnt += 1

#     return cnt  

#############
# Explanation
#############

# Intuition
# The problem asks us to count "symmetric" integers within a given range `[low, high]`. A number is symmetric if the sum of the digits in its first half equals the sum of the digits in its second half. This condition can only be met if the number has an even number of digits.
# The core idea is to iterate through every number from `low` to `high`, check if it's a candidate for being symmetric (i.e., has an even number of digits), and if so, perform the sum comparison.

# Walkthrough
# 1. Initialize a counter, `count`, to 0.
# 2. Loop through each integer `num` from `low` to `high` (inclusive).
# 3. For each `num`, convert it to its string representation, `s`, to easily access its digits.
# 4. Check the number of digits, `n = len(s)`. If `n` is odd, the number cannot be symmetric, so we `continue` to the next number in the loop.
# 5. If `n` is even, find the midpoint `mid = n // 2`.
# 6. Split the string `s` into two halves: `left_half` (from the start to `mid`) and `right_half` (from `mid` to the end).
# 7. Calculate the sum of the digits for each half. This involves converting each character back to an integer before summing.
# 8. Compare the two sums. If `left_sum` equals `right_sum`, we have found a symmetric integer, so we increment our `count`.
# 9. After the loop finishes, `count` will hold the total number of symmetric integers found in the range. Return `count`.

# Walkthrough Example
# Let's check `num = 1212` in a given range:
# 1. `s = "1212"`, `n = 4`. `n` is even.
# 2. `mid = 4 // 2 = 2`.
# 3. `left_half = s[:2] = "12"`. `right_half = s[2:] = "12"`.
# 4. `left_sum = 1 + 2 = 3`.
# 5. `right_sum = 1 + 2 = 3`.
# 6. The sums are equal. Increment `count`.

# Let's check `num = 1220`:
# 1. `s = "1220"`, `n = 4`. `n` is even.
# 2. `mid = 2`.
# 3. `left_half = "12"`, `right_half = "20"`.
# 4. `left_sum = 1 + 2 = 3`.
# 5. `right_sum = 2 + 0 = 2`.
# 6. Sums are not equal. Do not increment `count`.

# Time Complexity: O((h - l) * d)
# We iterate through the range of numbers from `high` to `low` (h - l). For each number, we do work proportional to its number of digits, `d`.

# Space Complexity: O(d)
# For each number, we store its string representation, which requires space proportional to the number of digits, `d`. This is the dominant space requirement.