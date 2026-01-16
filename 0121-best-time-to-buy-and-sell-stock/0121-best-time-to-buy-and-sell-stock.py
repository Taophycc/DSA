class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        l , r = 0, 1
        max_profit = 0

        while r < n:
            if prices[l] < prices[r]:
                curr_profit = prices[r] - prices[l]
                max_profit = max(max_profit, curr_profit)
            else:
                l=r
            r+=1
        return max_profit