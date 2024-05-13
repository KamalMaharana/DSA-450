class Solution:
    def matrixScore(self, grid: List[List[int]]) -> int:
        n = len(grid)
        m = len(grid[0])
        for i in range(n):
            if grid[i][0] == 0:
                # flip the row
                for j in range(m):
                    grid[i][j] = 0 if grid[i][j] else 1
        
        for j in range(m):
            ones = 0
            for i in range(n):
                if grid[i][j]:
                    ones += 1
            zeros = n - ones
            if zeros > ones:
                # flip the column
                for i in range(n):
                    grid[i][j] = 0 if grid[i][j] else 1
        
        # generate the number
        res = 0
        for r in range(n):
            num = ""
            for c in range(m):
                num += str(grid[r][c])
            
            res += int(num, 2)
                
        return res