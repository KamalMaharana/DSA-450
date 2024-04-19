def dfs(grid, i, j):
        if(i < 0 or i >= len(grid) or j < 0 or j >= len(grid[0]) or grid[i][j] == '0'):
            return 0
        grid[i][j] = "0"
        dfs(grid, i+1, j)
        dfs(grid, i, j+1)
        dfs(grid, i-1, j)
        dfs(grid, i, j-1)
        return 1
    
def sol(grid):
    ilands = 0
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if(grid[i][j] == "1"):
                ilands += dfs(grid, i, j)
        
    return ilands
    
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        return sol(grid)
    