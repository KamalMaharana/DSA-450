class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        mini = prices[0]
        profit = 0
        for i in range(1, len(prices)):
            curr = prices[i]
            mini = min(curr, mini)
            profit = max(profit, curr - mini)
        return profit