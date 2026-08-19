class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        i, j = 0, 1
        n = len(prices)

        max_profit = 0
        while j < n:
            if prices[i] > prices[j]:
                i = j
                j = i + 1
            else:
                max_profit = max(max_profit, prices[j] - prices[i])
                j += 1
        return max_profit