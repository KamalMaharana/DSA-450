class Solution:
    def winnerSquareGame(self, n: int) -> bool:
        dp = {}
        
        def dfs(state):
            if state == 0:
                return False
            
            if state in dp:
                return dp[state]
            
            winner = False
            for i in range(1, int(math.sqrt(state)) + 1):
                if not dfs(state - i*i):
                    winner = True
                    break
            
            dp[state] = winner
            return dp[state]
        
        return dfs(n)