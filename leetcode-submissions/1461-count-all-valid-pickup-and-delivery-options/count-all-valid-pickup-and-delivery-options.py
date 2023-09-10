class Solution:
    def countOrders(self, n: int) -> int:
        MOD = 10**9 + 7
        dp = [0] * (n + 1)
        dp[1] = 1
        # dp[2] = 6
        for i in range(2, len(dp)):
            possible_spaces = ((i - 1) * 2) + 1
            count = (possible_spaces * (possible_spaces + 1))//2
            dp[i] = dp[i - 1] * count
        
        return dp[n] % MOD