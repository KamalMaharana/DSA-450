class Solution:
    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        row = len(grid)
        col = len(grid[0])
        count = row * col
        k = k % count
        res = [[None for i in range(col)] for j in range(row)]
        pos_map = {}
        n = 0
        n_to_pos = {}
        for i in range(row):
            for j in range(col):
                pos_map[n] = (i, j)
                n_to_pos[(i,j)] = n
                n += 1
        
        for i in range(row):
            for j in range(col):
                n = n_to_pos[(i,j)]
                pos = (n + k) % count
                # print(pos)
                x, y = pos_map[pos]
                res[x][y] = grid[i][j]
        
        return res
                