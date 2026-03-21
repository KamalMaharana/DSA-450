class Solution:
    def reverseSubmatrix(self, grid: List[List[int]], x: int, y: int, k: int) -> List[List[int]]:
        # x is the starting row, y is the starting column
        # We only need to iterate through half of the rows to swap them
        for i in range(k // 2):
            row1 = x + i
            row2 = x + k - 1 - i
            
            # Swap the elements in the k columns for these two rows
            for j in range(y, y + k):
                grid[row1][j], grid[row2][j] = grid[row2][j], grid[row1][j]
                
        return grid