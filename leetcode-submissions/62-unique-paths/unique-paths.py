class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        def isend(i, j):
            return i == m - 1 and j == n - 1
        @cache
        def dfs(i, j):
            # print(i, j)
            if isend(i, j):
                return 1
            if i == m - 1:
                a = dfs(i, j + 1)
                return a
            elif j == n - 1:
                b = dfs(i + 1, j)
                return b
            a = dfs(i + 1, j)
            b = dfs(i, j + 1)
            return a + b
        return dfs(0, 0)