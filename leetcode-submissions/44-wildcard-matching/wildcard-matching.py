class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        @cache
        def dfs(i, j):
            if i == len(s) and j == len(p):
                return True
            
            if (i == len(s) and j != len(p) and p[j] != "*") or (i != len(s) and j == len(p)):
                return False

            ch = p[j]
            if ch == "*":
                for k in range(i, len(s) + 1):
                    if dfs(k, j + 1):
                        return True
            elif ch == "?":
                if dfs(i + 1, j + 1):
                    return True
            else:
                if s[i] == p[j] and dfs(i + 1, j + 1):
                    return True
            return False
        
        return dfs(0, 0)