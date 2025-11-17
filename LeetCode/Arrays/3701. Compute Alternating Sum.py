# Difficulty - EASY

# def alternatingSum(nums):
#         sum = 0

#         for x, num in enumerate(nums):
#             if x % 2 == 0:
#                 sum += num
#             else:
#                 sum += -num
                
#         return sum

#############
# Intuition
#############

# The problem asks us to compute an alternating sum of the elements in an array. This means we add the first element, subtract the second, add the third, and so on.

# We can iterate through the array and keep track of the index of each element. If the index is even, we add the element to our sum. If the index is odd, we subtract the element from our sum.

# Walkthrough
# 1. Initialize a variable `sum` to 0. This will store the alternating sum.
# 2. Iterate through the array `nums` using `enumerate` to get both the index `x` and the value `num` of each element.
# 3. For each element, check if its index `x` is even or odd.
# 4. If `x` is even (i.e., `x % 2 == 0`), add the `num` to `sum`.
# 5. If `x` is odd (i.e., `x % 2 != 0`), subtract the `num` from `sum` (or add its negation).
# 6. After iterating through all the numbers, the `sum` variable will hold the final alternating sum.
# 7. Return `sum`.

# Example
# nums = [1, 2, 3, 4, 5]
# 1. sum = 0
# 2. x = 0, num = 1. 0 is even. sum = 0 + 1 = 1.
# 3. x = 1, num = 2. 1 is odd. sum = 1 - 2 = -1.
# 4. x = 2, num = 3. 2 is even. sum = -1 + 3 = 2.
# 5. x = 3, num = 4. 3 is odd. sum = 2 - 4 = -2.
# 6. x = 4, num = 5. 4 is even. sum = -2 + 5 = 3.
# 7. Return 3.

# Time Complexity: O(n)
# We iterate through the input array `nums` once, where n is the number of elements in the array.

# Space Complexity: O(1)
# We are not using any extra space that scales with the input size. The space used is constant for the `sum` variable.
