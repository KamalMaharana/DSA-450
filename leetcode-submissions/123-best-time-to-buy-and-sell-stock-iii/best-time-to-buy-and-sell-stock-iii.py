class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l = len(prices)
        @cache
        def dfs(i, buying, k):
            if i == l: return 0
            
            if k == 0:
                return 0

            skip = dfs(i + 1, buying, k)

            if buying:
                profit = -prices[i] + dfs(i + 1, not buying, k)
            else:
                profit = +prices[i] + dfs(i + 1, not buying, k - 1)

            return max(skip, profit)
        
        return dfs(0, True, 2)

