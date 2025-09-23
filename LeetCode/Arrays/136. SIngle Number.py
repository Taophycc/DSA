# Difficulty - EASY

# # --- Brute-Force Solution ---
# # def singleNumber(self, nums: List[int]) -> int:
# #     n=len(nums)
# #     for i in range(n):
# #         cnt = 0
# #         for j in range(n):
# #             if nums[i] == nums[j]:
# #                 cnt += 1
# #         if cnt == 1:
# #             return nums[i]
# #
# # **Intuition:**
# # For each element in the array, iterate through the entire array again to count its occurrences.
# # If the count for an element is exactly one, it's the single number.
# #
# # **Complexity:**
# # - Time: O(n^2), because of the nested loops where for each element, we search the whole array.
# # - Space: O(1), as no extra space is used.


# # --- Better Solution (Hashing) ---
# # def singleNumber(self, nums: List[int]) -> int:
# #     n=len(nums)
# #     hashMap = {}
# #     for num in nums:
# #         hashMap[num] = hashMap.get(num,0)+1
# #     for num, count in hashMap.items():
# #         if count == 1:
# #             return num
# #     return -1
# #
# # **Intuition:**
# # Use a hash map to store the frequency of each number. We iterate through the array once to build the map,
# # then iterate through the map's items to find the number with a frequency of 1.
# #
# # **Complexity:**
# # - Time: O(n), because we iterate through the list once to build the map and once to check it.
# # - Space: O(n), as the hash map can store up to n/2 + 1 unique numbers.


# # --- Optimal Solution (XOR) ---
# # def singleNumber(self, nums: List[int]) -> int:
# #     xor = 0
# #     for num in nums:
# #         xor ^= num
# #     return xor
# #
# # **Intuition:**
# # This solution uses the properties of the bitwise XOR (^) operator:
# # 1. A number XORed with itself is 0 (e.g., `5 ^ 5 = 0`).
# # 2. A number XORed with 0 is the number itself (e.g., `5 ^ 0 = 5`).
# #
# # When we XOR all the numbers in the array, every number that appears twice will cancel itself out, leaving 0.
# # The final result of the XOR chain will be the single number XORed with 0, which is just the single number itself.
# #
# # **Example Walkthrough:** `nums = [4, 1, 2, 1, 2]`
# # - `xor` starts at 0.
# # - `xor = 0 ^ 4` -> `xor` is 4.
# # - `xor = 4 ^ 1` -> `xor` is 5.
# # - `xor = 5 ^ 2` -> `xor` is 7.
# # - `xor = 7 ^ 1` -> `xor` is 6. (because 5^2^1 = (4^1)^2^1 = 4^2)
# # - `xor = 6 ^ 2` -> `xor` is 4. (because 4^2^2 = 4)
# # Let's trace the bits: (4=100, 1=001, 2=010)
# #   000 ^ 100 = 100 (4)
# #   100 ^ 001 = 101 (5)
# #   101 ^ 010 = 111 (7)
# #   111 ^ 001 = 110 (6)
# #   110 ^ 010 = 100 (4)
# # The final result is 4, which is the single number.
# #
# # **Complexity:**
# # - Time: O(n), for a single pass through the array.
# # - Space: O(1), as no extra space is needed.