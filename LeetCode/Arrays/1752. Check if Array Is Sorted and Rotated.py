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
