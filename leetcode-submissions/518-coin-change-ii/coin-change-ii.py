class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        
        def f(ind, target, coins, dp):
            if dp[ind][target] != -1:
                return dp[ind][target]

            if ind == 0:
                dp[ind][target] = 1 if target % coins[ind] == 0 else 0
                return dp[ind][target]
            
            notTake = f(ind - 1, target, coins, dp)
            take = 0
            if coins[ind] <= target:
                take = f(ind, target - coins[ind], coins, dp)
            dp[ind][target] = take + notTake
            return dp[ind][target]
        
        n = len(coins)
        T = amount
        dp = [[-1 for _ in range(T + 1)] for _ in range(n)]
        res = f(n - 1, amount, coins, dp)
        return res