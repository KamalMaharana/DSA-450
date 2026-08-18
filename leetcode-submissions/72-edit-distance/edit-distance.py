class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        m, n = len(word1), len(word2)
        
        # cache[i][j] will store the edit distance of word1[:i] and word2[:j]
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        
        # Base cases: converting prefix to/from an empty prefix
        for i in range(m + 1):
            dp[i][0] = i  # Deleting all i characters of word1
        for j in range(n + 1):
            dp[0][j] = j  # Inserting all j characters of word2
            
        # Iterate forward from 1 to m and 1 to n
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if word1[i - 1] == word2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1]
                else:
                    insert = dp[i][j - 1]
                    delete = dp[i - 1][j]
                    replace = dp[i - 1][j - 1]
                    dp[i][j] = 1 + min(insert, delete, replace)
                    
        return dp[m][n]