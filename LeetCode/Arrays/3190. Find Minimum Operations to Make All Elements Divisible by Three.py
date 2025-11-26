# Difficulty - EASY

def minimumOperations(nums):
    operations = 0
    for num in nums:
        if num % 3 != 0:
            operations += 1
    return operations

#############
# Explanation
#############

# Intuition
# The goal is to make every number in the array divisible by 3 using the fewest operations. We can either add 1 or subtract 1.
# For any number, we can determine the required operations:
# - If `num % 3 == 0` (e.g., 3, 6, 9), it's already divisible by 3. It needs 0 operations.
# - If `num % 3 == 1` (e.g., 1, 4, 7), we can subtract 1 to make it divisible by 3. This is one operation.
# - If `num % 3 == 2` (e.g., 2, 5, 8), we can add 1 to make it divisible by 3. This is also one operation.
# In summary, any number that is not already divisible by 3 requires exactly one operation. Therefore, the total minimum operations is simply the count of numbers that are not divisible by 3.

# Walkthrough
# 1. Initialize a counter variable, `operations`, to 0.
# 2. Iterate through each `num` in the input array `nums`.
# 3. For each `num`, check its remainder when divided by 3 (`num % 3`).
# 4. If the remainder is not 0, it means the number is not divisible by 3 and needs one operation. Increment the `operations` counter.
# 5. If the remainder is 0, the number is already divisible by 3, so we do nothing.
# 6. After the loop finishes, `operations` holds the total count of numbers that needed a change. Return this count.

# Walkthrough Example
# nums = [1, 2, 3, 4]
# 1. Initialize `operations = 0`.
# 2. `num = 1`. `1 % 3` is `1` (not 0). Increment `operations` to 1.
# 3. `num = 2`. `2 % 3` is `2` (not 0). Increment `operations` to 2.
# 4. `num = 3`. `3 % 3` is `0`. Do nothing.
# 5. `num = 4`. `4 % 3` is `1` (not 0). Increment `operations` to 3.
# 6. Loop finishes. Return `operations`, which is 3.

# Time Complexity: O(n)
# We perform a single pass through the array, so the time complexity is linear with respect to the number of elements, `n`.

# Space Complexity: O(1)
# We only use a single counter variable (`operations`), so the amount of extra space is constant and does not scale with the input size.