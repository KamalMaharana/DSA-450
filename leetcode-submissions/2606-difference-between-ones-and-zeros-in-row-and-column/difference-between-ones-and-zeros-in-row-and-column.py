class Solution:
    def onesMinusZeros(self, grid: List[List[int]]) -> List[List[int]]:
        r = len(grid)
        c = len(grid[0])
        rows = [0] * r
        cols = [0] * c
        for i in range(r):
            for j in range(c):
                if grid[i][j]:
                    rows[i] += 1
                    cols[j] += 1
        
        for i in range(r):
            for j in range(c):
                diff = (rows[i] + cols[j]) - (c - rows[i] + r - cols[j])
                grid[i][j] = diff
        return grid