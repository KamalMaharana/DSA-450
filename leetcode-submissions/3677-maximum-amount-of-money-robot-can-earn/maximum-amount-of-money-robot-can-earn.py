class Solution:
    def maximumAmount(self, coins: List[List[int]]) -> int:
        m, n = len(coins), len(coins[0])
        
        # dp[i][j][k] = max coins at cell (i, j) with k neutralizations used
        # Initialize with -float('inf') as we can have negative total coins
        dp = [[[-float('inf')] * 3 for _ in range(n)] for _ in range(m)]
        
        for i in range(m):
            for j in range(n):
                # Base Case: Starting point
                if i == 0 and j == 0:
                    dp[0][0][0] = coins[0][0]
                    if coins[0][0] < 0:
                        dp[0][0][1] = 0
                    continue
                
                for k in range(3):
                    # Option 1: Move from Top (if within bounds)
                    if i > 0:
                        # Case A: Don't neutralize current cell
                        dp[i][j][k] = max(dp[i][j][k], dp[i-1][j][k] + coins[i][j])
                        # Case B: Neutralize current cell (if k > 0 and robber present)
                        if k > 0 and coins[i][j] < 0:
                            dp[i][j][k] = max(dp[i][j][k], dp[i-1][j][k-1])
                            
                    # Option 2: Move from Left (if within bounds)
                    if j > 0:
                        # Case A: Don't neutralize current cell
                        dp[i][j][k] = max(dp[i][j][k], dp[i][j-1][k] + coins[i][j])
                        # Case B: Neutralize current cell (if k > 0 and robber present)
                        if k > 0 and coins[i][j] < 0:
                            dp[i][j][k] = max(dp[i][j][k], dp[i][j-1][k-1])
                            
        # The answer is the maximum value reaching the bottom-right cell with 0, 1, or 2 neutralizations
        return max(dp[m-1][n-1])