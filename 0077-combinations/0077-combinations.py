class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        # choice - choose one number for available pool to add to combinations
        # constraints - can't reuse numbers and can't look backward
        # goal - current combination should have exactly k numbers in it
        
        res = []
        comb = []
        def backtrack(start):
            if k == len(comb):
                res.append(comb[:])
                return
            for num in range(start, n+1):
                comb.append(num)
                backtrack(num + 1)
                comb.pop()
        backtrack(1) 
        return res
                
