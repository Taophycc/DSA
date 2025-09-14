# Difficulty - EASY

# def check(self, nums: List[int]) -> bool:
#     c = 0
#     n = len(nums)
#     for i in range(n):
#         if nums[i] > nums[(i + 1) % len(nums)]:
#             c += 1
#             if c > 1:
#                 return False
#     return True

"""
### Explanation:
A sorted array that is rotated can have at most one "break" where an element is larger than the next one (considering the array as circular). This code counts these breaks.

- It iterates through the array, comparing each element `nums[i]` with the next `nums[(i + 1) % n]`. The modulo `%` handles the wrap-around from the last element to the first.
- A counter `c` is incremented for each break found.
- If `c` becomes greater than 1, it's impossible for the array to be a rotated sorted array, so it returns `False`.
- If the loop finishes with `c` being 0 (already sorted) or 1 (rotated), it returns `True`.

### Example: `nums = [3, 4, 5, 1, 2]`
1. `c` starts at 0.
2. The code finds a break at `i=2` where `nums[2]` (5) > `nums[3]` (1). `c` becomes 1.
3. The loop continues, but no more breaks are found.
4. The loop finishes, `c` is 1, so the function returns `True`.
"""