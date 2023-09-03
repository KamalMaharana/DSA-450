class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        @cache
        def dfs(i, j):
            # print(i,j)
            if i == n - 1:
                return matrix[i][j]
            
            result = inf
            for k in [-1, 0, 1]:
                new_idx = j + k
                if 0 <= new_idx < n:
                    result = min(result, dfs(i + 1, new_idx) + matrix[i][j])
            return result
        
        n = len(matrix)
        result = inf
        for i in range(n):
            result = min(result, dfs(0, i))
        return result