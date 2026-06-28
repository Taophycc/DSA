class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        permutations = []
        path = []
        
        def backtrack(index):
            if index == len(nums):
                permutations.append(list(path))
                return

            for num in nums:
                if num in path:
                    continue

                path.append(num)
                backtrack(index + 1)
                path.pop()

        backtrack(0)
        return permutations