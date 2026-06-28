class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        permutations = []
        path = []
        used = set()
        
        def backtrack():
            if len(path) == len(nums):
                permutations.append(list(path))
                return

            for num in nums:
                if num in used:
                    continue
                used.add(num)

                path.append(num)
                backtrack()
                path.pop()
                used.remove(num)

        backtrack()
        return permutations