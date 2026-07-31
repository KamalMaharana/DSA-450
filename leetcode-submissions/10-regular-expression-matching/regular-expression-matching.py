class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        @cache
        def dfs(i: int, j: int) -> bool:
            # Base Case 1: Reached end of pattern
            if j == len(p):
                return i == len(s)
            
            # Check if current characters match
            first_match = (i < len(s)) and (p[j] in {s[i], '.'})
            
            # Case 1: Next character in pattern is '*'
            if j + 1 < len(p) and p[j + 1] == '*':
                # Option A: Ignore 'x*' completely (0 matches) -> move j to j + 2
                # Option B: Match 1 instance and stay on '*' -> move i to i + 1 (requires first_match)
                return dfs(i, j + 2) or (first_match and dfs(i + 1, j))
            
            # Case 2: Regular character match or '.'
            return first_match and dfs(i + 1, j + 1)
            
        return dfs(0, 0)