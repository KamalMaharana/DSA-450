class Solution:
    def cherryPickup(self, grid: List[List[int]]) -> int:
        directions = [-1, 0, 1]
        dp = {}
        row = len(grid)
        col = len(grid[0])
        
        def isValidRow(index):
            return 0 <= index < len(grid)
        
        def isValidColumn(index):
            return 0 <= index < len(grid[0])
        
        def isValid(i, j):
            return 0 <= i < len(grid) and 0 <= j < len(grid[0])
        
        # As we are always going down the ROW by 1 for both robots.
        # And both robots are always at same ROW, so we have only 'x' in dfs
        # instead of x1, x2 for robot1 and robot2
        def dfs(x, y1, y2):
            
            if (x, y1, y2) in dp:
                return dp[(x, y1, y2)]
            
            
            # if not isValidRow(x) or not isValidColumn(y1) or not isValidColumn(y2): 
            #     return 0
            if not isValid(x, y1) or not isValid(x, y2): 
                return 0
            
            maxi = 0
            for y1_new in directions:
                for y2_new in directions:
                    maxi = max(maxi, dfs(x + 1, y1 + y1_new, y2 + y2_new))
                    
            # As both robot will always be at same ROW, but if we reach at same column
            # SO here as only 1 ROBOT can pick the cheery, so we only counting
            # grid[x][y] once.
            res = 0
            if y1 == y2:
                res = maxi + grid[x][y1]
            
            else:
                res = maxi + grid[x][y1] + grid[x][y2]
            
            dp[(x, y1, y2)] = res
            return res
        
        return dfs(0, 0, col - 1)