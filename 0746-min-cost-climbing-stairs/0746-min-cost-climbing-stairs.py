class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
        if n <= 1:
            return 0

        prev2 = cost[0]
        prev1 = cost[1]

        for i in range(2, n+1):
            curr_cost = cost[i] if i < n else 0
            current = curr_cost + min(prev1, prev2)
            prev2 = prev1
            prev1 = current
        return prev1