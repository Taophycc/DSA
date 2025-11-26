# DIfficulty - EASY

# def containsNearbyDuplicate(nums, k):         
#     nums_map = {}

#     for i, num in enumerate(nums):
#         if num in nums_map:
#             prev_index = nums_map[num]
#             if abs(i - prev_index) <= k:
#                 return True

#         nums_map[num] = i
        
#     return False    

#############
# Optimal
#############

# Intuition
# We need to find two identical numbers that are at most `k` indices apart. As we iterate through the array, we need to remember not just the numbers we've seen, but also their last known positions. A hash map is ideal for this, mapping each number to its most recent index. When we encounter a number that's already in our map, we can check if the distance between the current index and the stored index is less than or equal to `k`. If it is, we've found our pair. If not, we update the map with the current index for that number, as it's the most recent one.

# Walkthrough
# 1. Create an empty hash map called `nums_map` to store `number: index` pairs.
# 2. Iterate through the input array `nums` with their indices (`i`) and values (`num`).
# 3. For each `num`, check if it already exists as a key in `nums_map`.
# 4. If it does, it means we've seen this number before. Calculate the difference between the current index `i` and the previously stored index `nums_map[num]`.
# 5. If this difference is less than or equal to `k`, we have found a valid pair, so we return `True`.
# 6. If the number is not in the map, or if the index difference was greater than `k`, we update the map with the current number and its index: `nums_map[num] = i`. This ensures we always have the most recent index for any future duplicates we might find.
# 7. If the loop completes without returning `True`, it means no such pair exists, so we return `False`.

# Walkthrough Example
# nums = [1, 2, 3, 1], k = 3
# 1. `i = 0, num = 1`. `1` is not in `nums_map`. `nums_map` becomes `{1: 0}`.
# 2. `i = 1, num = 2`. `2` is not in `nums_map`. `nums_map` becomes `{1: 0, 2: 1}`.
# 3. `i = 2, num = 3`. `3` is not in `nums_map`. `nums_map` becomes `{1: 0, 2: 1, 3: 2}`.
# 4. `i = 3, num = 1`. `1` is in `nums_map`. The stored index is `0`. Check `abs(3 - 0) <= 3`. `3 <= 3` is `True`. Return `True`.

# Time Complexity: O(n)
# We iterate through the input array `nums` once. Each dictionary operation (lookup and insertion) takes, on average, O(1) time.

# Space Complexity: O(n)
# In the worst-case scenario (no duplicates or duplicates are far apart), the `nums_map` could store up to `n` key-value pairs. In a better case where the number of unique elements `u` is much smaller than `n`, the space is O(u).