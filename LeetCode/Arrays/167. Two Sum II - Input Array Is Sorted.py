# Difficulty - MEDIUM

# def twoSum(numbers, target):
#         n = len(numbers)
#         left, right = 0, n - 1

#         while left < right: 
#             currentSum = numbers[left] + numbers[right]

#             if currentSum == target:
#                 return [left + 1, right + 1]
#             elif currentSum < target:    
#                 left += 1
#             else:
#                 right -= 1    

#         return []

###############
# Optimal
###############

# Intuition
# Since the array is sorted, we can use a two-pointer approach to find the target sum efficiently.
# We start with one pointer at the beginning of the array and another at the end.
# We then move the pointers inward based on the comparison of their sum with the target.

# Walkthrough
# 1. Initialize two pointers, `left` at the start of the array (index 0) and `right` at the end (index n-1).
# 2. Loop as long as `left` is less than `right`.
# 3. Calculate the `currentSum` of the values at the `left` and `right` pointers.
# 4. If `currentSum` equals the `target`, we have found the solution. The problem asks for 1-based indices, so we return `[left + 1, right + 1]`.
# 5. If `currentSum` is less than the `target`, we need a larger sum. Since the array is sorted, we move the `left` pointer one step to the right to include a larger number in the sum.
# 6. If `currentSum` is greater than the `target`, we need a smaller sum. We move the `right` pointer one step to the left to include a smaller number.
# 7. If the loop finishes without finding a solution, it means no such pair exists, and we return an empty list.

# Walkthrough Example
# numbers = [2, 7, 11, 15], target = 9
# 1. left = 0, right = 3. currentSum = numbers[0] + numbers[3] = 2 + 15 = 17. 17 > 9, so right becomes 2.
# 2. left = 0, right = 2. currentSum = numbers[0] + numbers[2] = 2 + 11 = 13. 13 > 9, so right becomes 1.
# 3. left = 0, right = 1. currentSum = numbers[0] + numbers[1] = 2 + 7 = 9. 9 == 9. Return [left + 1, right + 1] which is [1, 2].

# Time Complexity: O(n)
# The `left` and `right` pointers together traverse the array at most once. In each iteration, we do a constant amount of work.

# Space Complexity: O(1)
# We only use a constant amount of extra space for the `left` and `right` pointers and the `currentSum` variable, regardless of the input size.