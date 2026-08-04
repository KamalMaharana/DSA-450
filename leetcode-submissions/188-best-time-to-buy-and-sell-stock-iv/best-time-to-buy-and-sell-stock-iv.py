class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        n = len(prices)
        if not prices or k == 0:
            return 0
        
        # Optimization: If k >= n // 2, it's equivalent to unlimited transactions
        if k >= n // 2:
            return sum(max(prices[i + 1] - prices[i], 0) for i in range(n - 1))
        
        dp = {}
        
        def dfs(i: int, buying: bool, k: int) -> int:
            if i >= n or k == 0:
                return 0
            
            if (i, buying, k) in dp:
                return dp[(i, buying, k)]
            
            # Choice 1: Skip day i (do nothing)
            skip = dfs(i + 1, buying, k)
            
            if buying:
                # Choice 2: Buy stock on day i
                action = dfs(i + 1, False, k) - prices[i]
            else:
                # Choice 2: Sell stock on day i (decrements k, advances to i + 1)
                action = dfs(i + 1, True, k - 1) + prices[i]
            
            dp[(i, buying, k)] = max(skip, action)
            return dp[(i, buying, k)]
            
        return dfs(0, True, k)