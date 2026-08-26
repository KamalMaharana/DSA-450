class Solution:
    def knightProbability(self, n: int, k: int, row: int, column: int) -> float:
        dp = {}
        dirs = ((-2,-1),(-1,-2),(1,-2),(2,-1),(2,1),(1,2),(-1,2),(-2,1))
        def isValid(r, c):
            return 0 <= r < n and 0 <= c < n

        def dfs(r, c, k):
            if not isValid(r, c):
                return 0
            
            if k == 0:
                return 1

            if (r, c, k) in dp:
                return dp[(r, c, k)]
            
            rate = 0
            for x, y in dirs:
                # 8 directions from each cell, so 1/8 == 0.125 is the probability of each cell
                # if the cell is valid, and probability multiplies
                rate += 0.125 * dfs(r + x, c + y, k - 1)

            dp[(r, c, k)] = rate
            return rate
        
        result = dfs(row, column, k)
        print(dp)
        return result