class Solution:
    def findRotation(self, mat: List[List[int]], target: List[List[int]]) -> bool:
        def rotate_matrix(grid):
            n = len(grid)
            # 1. Transpose (Corrected range)
            for i in range(n):
                for j in range(i + 1, n): # Start j from i + 1
                    grid[i][j], grid[j][i] = grid[j][i], grid[i][j]
            
            # 2. Reverse rows
            for r in range(n):
                grid[r].reverse() # Shorthand for grid[r][::-1] in-place
            
            return grid
        
        def is_matching(src, target):
            row = len(src)
            col = len(src[0])
            for i in range(row):
                for j in range(col):
                    if src[i][j] != target[i][j]:
                        return False
            return True
        
        if is_matching(mat, target):
            return True

        for i in range(4):
            mat = rotate_matrix(mat)
            if is_matching(mat, target):
                return True
        return False
