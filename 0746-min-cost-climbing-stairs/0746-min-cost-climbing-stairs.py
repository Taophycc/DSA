class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
        cache = {}

        def dp(n):
            if n == 0:
                return cost[0]
            if n == 1:
                return cost[1]

            if n in cache:
                return cache[n]

            curr_cost = cost[n] if n < len(cost) else 0

            cache[n] = curr_cost + min(dp(n-1), dp(n-2))
            return cache[n]
        return dp(n)