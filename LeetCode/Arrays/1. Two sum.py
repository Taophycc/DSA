
# Difficulty - EASY

# Brute force 
# def twoSum_brute_force( nums, target):
#     n = len(nums)

#     for i in range(n-1):
#         for j in range(i+1, n):
#             if nums[i] + nums[j] == target:
#                 return [i,j]
#     return        


# Optimal
# def twoSum_optimal(nums, target):
#     num_map = {}

#     for i, num in enumerate(nums):
#         complement = target - num

#         if complement in num_map:
#             return [num_map[complement],i]
    
#         num_map[num] = i 
#     return

# #############
# Brute Force
# #############

# Intuition
# The most straightforward approach is to check every possible pair of numbers in the array to see if they sum up to the target.

# Walkthrough
# 1. We use two nested loops to iterate through all possible pairs of indices (i, j) in the array.
# 2. For each pair, we check if the sum of the numbers at these indices (nums[i] + nums[j]) equals the target.
# 3. If we find such a pair, we return their indices [i, j].
# 4. If we iterate through all pairs without finding a solution, we return an empty list or handle it as the problem requires.

# Time Complexity: O(n^2)
# We have two nested loops, where the outer loop runs n-1 times and the inner loop runs up to n-1 times for each outer iteration. This results in a quadratic time complexity.

# Space Complexity: O(1)
# We are not using any extra space that scales with the input size. The space used is constant.

# #############
# Optimal
# #############

# Intuition
# A better approach is to use a hash map to store the numbers we've seen and their indices.
# For each number in the array, we calculate its complement (target - number).
# If the complement is already in our hash map, we've found our pair.
# If not, we add the current number and its index to the hash map.

# Walkthrough
# 1. Create an empty hash map called `num_map`.
# 2. Iterate through the input array `nums` with their indices (`i`) and values (`num`).
# 3. For each number, calculate the `complement` needed to reach the `target`.
# 4. Check if this `complement` exists as a key in `num_map`.
# 5. If it does, we have found our pair. The first number is the complement, and the second is the current number. We return the index of the complement (stored in `num_map`) and the index of the current number (`i`).
# 6. If the `complement` is not in `num_map`, it means we haven't found the pair yet. We add the current number `num` as a key to `num_map` and its index `i` as the value. This is for future iterations to check against.
# 7. If we get through the whole loop without finding a pair, we return an empty list (or whatever the problem requires for no solution).

# Walkthrough Example
# nums = [2, 7, 11, 15], target = 9
# 1. i = 0, num = 2, complement = 7. 7 is not in num_map. num_map becomes {2: 0}.
# 2. i = 1, num = 7, complement = 2. 2 is in num_map. Return [num_map[2], 1] which is [0, 1].

# Time Complexity: O(n)
# We iterate through the list of numbers once. Each lookup and insertion in the hash map is, on average, O(1).

# Space Complexity: O(n)
# In the worst-case scenario, we might have to store all `n` numbers in the hash map. This happens if the pair is found at the very end of the array or not at all.
