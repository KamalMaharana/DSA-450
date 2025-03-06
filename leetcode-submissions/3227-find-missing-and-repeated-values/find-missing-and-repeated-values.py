class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        seen = set()
        a = 0
        b = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                val = grid[i][j]
                if val in seen:
                    a = val
                seen.add(val)
        n = len(grid)
        for i in range(1, n * n + 1):
            if i not in seen:
                return [a, i]
        