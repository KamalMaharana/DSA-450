class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        @cache
        def dfs(i: int, j: int) -> int:
            # Reached end of target: successfully formed a valid subsequence
            if j == len(t):
                return 1
            # Reached end of source without completing target
            if i == len(s):
                return 0
            
            # Choice 1: Always can skip current character s[i]
            res = dfs(i + 1, j)
            
            # Choice 2: Use s[i] if it matches t[j]
            if s[i] == t[j]:
                res += dfs(i + 1, j + 1)
                
            return res

        return dfs(0, 0)