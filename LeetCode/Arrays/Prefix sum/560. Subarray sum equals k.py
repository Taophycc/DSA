# Difficult - Medium

# def subarraySum(self, nums: List[int], k: int) -> int:
#     res = 0
#     curr_sum = 0
#     prefix_sums = {0:1}

#     for n in nums:
#         curr_sum += n
#         diff = curr_sum - k

#         res += prefix_sums.get(diff, 0)
#         prefix_sums[curr_sum] = 1 + prefix_sums.get(curr_sum, 0)


#     return res

#############
# Intuition
#############

# The problem asks us to find the total number of continuous subarrays whose sum equals a given integer `k`.

# A naive approach would be to check every possible subarray, calculate its sum, and see if it equals `k`. This would involve nested loops and would be O(n^2).

# A more efficient approach uses the concept of prefix sums and a hash map.
# The idea is that if the sum of elements from index `i` to `j` (inclusive) is `k`, then `sum(0, j) - sum(0, i-1) = k`.
# This can be rewritten as `sum(0, i-1) = sum(0, j) - k`.

# So, as we iterate through the array and calculate the `curr_sum` (which is `sum(0, j)`), we can check if there was a previous `prefix_sum` (which would be `sum(0, i-1)`) such that `prefix_sum = curr_sum - k`.
# We use a hash map to store the frequency of each `prefix_sum` encountered so far.

# Walkthrough
# 1. Initialize `res` (result) to 0. This will store the count of subarrays that sum to `k`.
# 2. Initialize `curr_sum` to 0. This will keep track of the sum of elements from the beginning of the array up to the current element.
# 3. Initialize `prefix_sums` as a hash map (dictionary in Python). We put `{0: 1}` into it initially. This handles the case where the subarray itself starts from index 0 and its sum is `k`. If `curr_sum - k` is 0, it means the current `curr_sum` is `k`, and we found one such subarray.

# 4. Iterate through each number `n` in the input array `nums`:
#    a. Update `curr_sum` by adding the current number `n`: `curr_sum += n`.
#    b. Calculate `diff = curr_sum - k`. This `diff` represents the `prefix_sum` we are looking for. If we find a `prefix_sum` equal to `diff`, it means the subarray between that `prefix_sum`'s end and the current index sums to `k`.
#    c. Add the count of `diff` from `prefix_sums` to `res`. If `diff` is not in `prefix_sums`, `get(diff, 0)` will return 0, so `res` won't change.
#    d. Increment the count of `curr_sum` in `prefix_sums`. If `curr_sum` is not already a key, it's added with a count of 1. Otherwise, its count is incremented.

# 5. After iterating through all numbers, return `res`.

# Example
# nums = [1, 1, 1], k = 2

# Initial: res = 0, curr_sum = 0, prefix_sums = {0: 1}

# 1. n = 1:
#    - curr_sum = 0 + 1 = 1
#    - diff = 1 - 2 = -1
#    - res += prefix_sums.get(-1, 0) => res = 0 + 0 = 0
#    - prefix_sums[1] = 1 + prefix_sums.get(1, 0) => prefix_sums = {0: 1, 1: 1}

# 2. n = 1:
#    - curr_sum = 1 + 1 = 2
#    - diff = 2 - 2 = 0
#    - res += prefix_sums.get(0, 0) => res = 0 + 1 = 1 (Subarray [1, 1] sums to 2)
#    - prefix_sums[2] = 1 + prefix_sums.get(2, 0) => prefix_sums = {0: 1, 1: 1, 2: 1}

# 3. n = 1:
#    - curr_sum = 2 + 1 = 3
#    - diff = 3 - 2 = 1
#    - res += prefix_sums.get(1, 0) => res = 1 + 1 = 2 (Subarray [1, 1] (from index 1) sums to 2)
#    - prefix_sums[3] = 1 + prefix_sums.get(3, 0) => prefix_sums = {0: 1, 1: 1, 2: 1, 3: 1}

# Return res = 2.

# Time Complexity: O(n)
# We iterate through the array once. Dictionary operations (insertion and lookup) take O(1) on average.

# Space Complexity: O(n)
# In the worst case, all prefix sums could be unique, leading to the hash map storing up to `n` entries.
