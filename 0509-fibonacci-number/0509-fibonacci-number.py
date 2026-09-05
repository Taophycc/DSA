class Solution:
    def fib(self, n: int) -> int:
        cache = {}
        
        def dfs(n):
            if n <= 1:
                return n
            if n in cache:
                return cache[n]
            
            left = dfs(n-1)
            right = dfs(n-2)

            cache[n] = left + right
            return cache[n]

        return dfs(n)