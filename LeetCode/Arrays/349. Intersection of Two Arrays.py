# Difficulty - EASY

# # Brute Force
# def intersection_brute_force( nums1, nums2):
#         arr = []
#         for num1 in nums1:
#             if num1 in nums2:
#                 arr.append(num1)

#         intersect = set(arr)

#         return list(intersect)

# # Optimal Solution 1
# def intersection_optimal_1( nums1, nums2):
#     setA = set(nums1)
#     setB = set(nums2)

#     common_element = setA & setB
            
#     return list(common_element)

# # Optimal Solution 2
# def intersection_optimal_2(nums1, nums2):
#         # checking to make sure nums1 is the smaller of the two arrays to reduce memory
#         if len(nums1) > len(nums2):
#             nums1 , nums2 = nums2, nums1

#         seen = set(nums1)    
#         result = set()

#         for num in nums2:
#             if num in seen:
#                 result.add(num)

#         return list(result)

#############
# Brute Force
#############

# Intuition
# The most straightforward approach is to iterate through each element of the first array and check if it exists in the second array. If it does, we add it to a list. To handle duplicates, we can convert the list to a set and then back to a list.

# Walkthrough
# 1. Create an empty list `arr`.
# 2. Iterate through each element `num1` in the first array `nums1`.
# 3. For each `num1`, check if it is present in the second array `nums2`.
# 4. If `num1` is in `nums2`, append `num1` to `arr`.
# 5. After checking all elements in `nums1`, `arr` will contain all common elements, including duplicates.
# 6. To get the unique intersection, convert `arr` to a set, and then convert it back to a list.
# 7. Return the resulting list.

# Time Complexity: O(n*m)
# For each element in `nums1` (length n), we search for it in `nums2` (length m). This results in a time complexity of O(n*m). The final conversion to a set takes O(k) where k is the number of elements in `arr`.

# Space Complexity: O(k)
# We use an extra list `arr` to store the common elements, where k is the number of common elements. The set also uses space.

####################
# Optimal Solution 1
####################

# Intuition
# A more efficient approach is to use sets. Sets provide a fast way to find the intersection of two collections. By converting both arrays to sets, we can use the built-in intersection operation.

# Walkthrough
# 1. Convert the first array `nums1` to a set, `setA`.
# 2. Convert the second array `nums2` to a set, `setB`.
# 3. Find the intersection of `setA` and `setB` using the `&` operator. This gives a new set containing only the elements present in both sets.
# 4. Convert the resulting set to a list.
# 5. Return the list.

# Time Complexity: O(n + m)
# It takes O(n) to convert `nums1` to a set and O(m) to convert `nums2` to a set. The intersection of two sets takes, on average, O(min(len(setA), len(setB))).

# Space Complexity: O(n + m)
# We create two sets, `setA` and `setB`, which store the unique elements of `nums1` and `nums2` respectively. In the worst case, all elements are unique, so the space complexity is O(n + m).

####################
# Optimal Solution 2
####################

# Intuition
# This approach is similar to the first optimal solution but optimizes for space. It ensures that the smaller of the two arrays is converted to a set, reducing the memory footprint. Then, it iterates through the larger array and checks for membership in the set.

# Walkthrough
# 1. Compare the lengths of `nums1` and `nums2`. If `nums1` is larger, swap them so that `nums1` is always the smaller array. This is a space optimization.
# 2. Convert the smaller array `nums1` into a set called `seen`.
# 3. Create an empty set called `result` to store the intersection.
# 4. Iterate through each element `num` in the larger array `nums2`.
# 5. For each `num`, check if it is present in the `seen` set.
# 6. If `num` is in `seen`, add it to the `result` set.
# 7. After iterating through all elements of `nums2`, convert the `result` set to a list.
# 8. Return the list.

# Time Complexity: O(n + m)
# It takes O(n) to create the `seen` set from `nums1` (assuming n is the length of the smaller array). Then, it takes O(m) to iterate through `nums2`. Checking for an element in a set is O(1) on average.

# Space Complexity: O(min(n, m))
# We create a set `seen` from the smaller of the two arrays. Therefore, the space used is proportional to the size of the smaller array.
