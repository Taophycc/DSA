# Difficulty - EASY

# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

# def firstBadVersion(n):
#     left, right = 1, n

#     while left < right:
#         mid = left + (right - left) // 2

#         if isBadVersion(mid):
#             right = mid
#         else:
#             left = mid + 1

#     return left

#############
# Intuition
#############

# The problem asks us to find the first bad version from a range of versions [1, n]. We are given an API `isBadVersion(version)` which returns `True` if the version is bad and `False` otherwise. We know that if a version is bad, all subsequent versions are also bad.

# This problem can be solved efficiently using binary search. The versions are sorted, and we have a way to "test" any version. This is a classic binary search scenario.

# We can define a search range with a `left` and `right` pointer. We'll repeatedly check the middle version of our range.
# - If the middle version is bad, it means the first bad version could be this middle version or any version before it. So, we narrow our search to the left half, including the middle version.
# - If the middle version is not bad, it means the first bad version must be after the middle version. So, we narrow our search to the right half.

# We continue this process until our search range converges to a single version, which will be the first bad version.

# Walkthrough
# 1. Initialize `left` to 1 and `right` to `n`. These represent the start and end of our search range.
# 2. We use a `while` loop that continues as long as `left` is less than `right`. This condition ensures that our search range has at least two elements.
# 3. Inside the loop, we calculate the middle index `mid`. We use `left + (right - left) // 2` to avoid potential integer overflow.
# 4. We call `isBadVersion(mid)` to check if the version at `mid` is bad.
# 5. If `isBadVersion(mid)` is `True`, it means `mid` could be the first bad version, or there might be one before it. So, we update `right = mid`. We don't do `mid - 1` because `mid` itself is a candidate for the first bad version.
# 6. If `isBadVersion(mid)` is `False`, it means all versions up to `mid` are good. The first bad version must be after `mid`. So, we update `left = mid + 1`.
# 7. The loop terminates when `left` and `right` become equal. At this point, `left` (or `right`) will be pointing to the first bad version.
# 8. Return `left`.

# Example
# n = 5, bad = 4
# isBadVersion(1) -> False
# isBadVersion(2) -> False
# isBadVersion(3) -> False
# isBadVersion(4) -> True
# isBadVersion(5) -> True

# 1. left = 1, right = 5
# 2. mid = 1 + (5 - 1) // 2 = 3. isBadVersion(3) is False. So, left = 3 + 1 = 4.
# 3. left = 4, right = 5
# 4. mid = 4 + (5 - 4) // 2 = 4. isBadVersion(4) is True. So, right = 4.
# 5. left = 4, right = 4. The loop terminates.
# 6. Return left, which is 4.

# Time Complexity: O(log n)
# Binary search reduces the search space by half in each iteration. This results in a logarithmic time complexity.

# Space Complexity: O(1)
# We are only using a few variables (`left`, `right`, `mid`) to store pointers. The space used is constant and does not scale with the input size `n`.
