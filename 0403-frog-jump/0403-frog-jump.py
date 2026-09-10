class Solution:
    def canCross(self, stones: List[int]) -> bool:
        stone_set = set(stones)

        cache = {}

        def dp(curr_stone, k):
            if curr_stone == stones[-1]:
                return True
            if curr_stone not in stone_set:
                return False
            
            if (curr_stone, k) in cache:
                return cache[(curr_stone, k)]
            
            for jump in (k-1, k, k+1):
                if jump > 0:
                    next_stone = curr_stone + jump

                    if dp(next_stone, jump):
                        return True

            cache[(curr_stone, k)] = False
            return False
        
        if stones[1] != 1:
            return False

        return dp(1,1)