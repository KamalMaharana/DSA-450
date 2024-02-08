class Solution:
    def numSquares(self, n: int) -> int:
        perfect_squares = [i*i for i in range(1, int(math.sqrt(n)) + 1)]
        dp = [float('inf')]*(n+1)
        dp[0] = 0
        dp[1] = 1
        for i in range(2, n + 1):
            for square in perfect_squares:
                dp[i] = min(dp[i], dp[i - square] + 1)
        return dp[n]