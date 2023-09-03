class Solution:
    def countSquares(self, matrix: List[List[int]]) -> int:
        dp = [[0 for i in range(len(matrix[0]) + 1)] for j in range(len(matrix)+1)]
        for i in range(1,len(matrix)+1):
            for j in range(1, len(matrix[0])+1):
                if matrix[i-1][j-1] == 1:
                    dp[i][j] = matrix[i-1][j-1] + min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1])
        
        sums = 0
        for i in dp:
            sums += sum(i)
        return sums
        