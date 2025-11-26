# Difficulty - EASY

# def containsDuplicate(nums):
#         seen = set()

#         for num in nums:
#             if num in seen:
#                 return True

#             seen.add(num)
            
#         return False      

#############
# Optimal
#############

# Intuition
# To find a duplicate, we need to keep track of the numbers we've already encountered. A hash set is perfect for this because it provides fast lookups (average O(1) time). As we iterate through the array, we can check if the current number is already in our set. If it is, we've found a duplicate. If not, we add it to the set and continue.

# Walkthrough
# 1. Create an empty hash set called `seen`.
# 2. Iterate through each number (`num`) in the input array `nums`.
# 3. For each `num`, check if it already exists in `seen`.
# 4. If it does, we have found a duplicate, and we can immediately return `True`.
# 5. If it doesn't, add the `num` to the `seen` set to mark that we have now encountered it.
# 6. If the loop finishes without finding any duplicates, it means all elements were unique. Return `False`.

# Walkthrough Example
# nums = [1, 2, 3, 1]
# 1. `num = 1`. `1` is not in `seen`. Add `1` to `seen`. `seen` is now `{1}`.
# 2. `num = 2`. `2` is not in `seen`. Add `2` to `seen`. `seen` is now `{1, 2}`.
# 3. `num = 3`. `3` is not in `seen`. Add `3` to `seen`. `seen` is now `{1, 2, 3}`.
# 4. `num = 1`. `1` is in `seen`. Return `True`.

# Time Complexity: O(n)
# We iterate through the input array `nums` once. Each set operation (add and check) takes, on average, O(1) time.

# Space Complexity: O(n)
# In the worst-case scenario (no duplicates), the `seen` set will store all `n` elements from the input array.