from collections import Counter

class Solution:
    def canPartitionGrid(self, grid: List[List[int]]) -> bool:
        R, C = len(grid), len(grid[0])
        row_sums = [sum(row) for row in grid]
        col_sums = [sum(grid[r][c] for r in range(R)) for c in range(C)]
        total_sum = sum(row_sums)

        def check(segments, is_row):
            # total_counts helps us get frequencies for Section 2 efficiently
            total_counts = Counter(x for row in grid for x in row)
            prefix_counts = Counter()
            prefix_sum = 0
            
            for i in range(len(segments) - 1):
                prefix_sum += segments[i]
                # Update counts for the current row/column added to Section 1
                if is_row:
                    for j in range(C): prefix_counts[grid[i][j]] += 1
                else:
                    for j in range(R): prefix_counts[grid[j][i]] += 1
                
                s1, s2 = prefix_sum, total_sum - prefix_sum
                
                # Check 3 Scenarios for this cut:
                # 1. Perfect Match
                if s1 == s2: return True
                
                # 2. Discount from Section 1 (s1 must be > s2)
                diff1 = s1 - s2
                if diff1 > 0 and prefix_counts[diff1] > 0:
                    if self.is_connected(diff1, 0, i + 1, is_row, grid):
                        return True
                
                # 3. Discount from Section 2 (s2 must be > s1)
                diff2 = s2 - s1
                if diff2 > 0:
                    # Section 2 counts = total - section 1
                    if (total_counts[diff2] - prefix_counts[diff2]) > 0:
                        if self.is_connected(diff2, i + 1, len(segments), is_row, grid):
                            return True
            return False

        return check(row_sums, True) or check(col_sums, False)

    def is_connected(self, val, start, end, is_row, grid):
        R, C = len(grid), len(grid[0])
        h = (end - start) if is_row else R
        w = C if is_row else (end - start)
        
        # Rule 1: If it's a 2D block (thick), any internal removal is connected
        if h > 1 and w > 1:
            return True
        
        # Rule 2: If it's a 1D strip, the value MUST be at an endpoint
        if is_row:
            if h == 1: # Horizontal strip: check left/right ends
                return grid[start][0] == val or grid[start][C-1] == val
            if w == 1: # Vertical strip: check top/bottom ends
                return grid[start][0] == val or grid[end-1][0] == val
        else:
            if w == 1: # Vertical strip: check top/bottom ends
                return grid[0][start] == val or grid[R-1][start] == val
            if h == 1: # Horizontal strip: check left/right ends
                return grid[0][start] == val or grid[0][end-1] == val
        return False