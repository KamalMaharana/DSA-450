class Solution:
    def minimumTime(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        if grid[1][0] > 1 and grid[0][1] > 1: return -1
        def reachable(i, j, visited):
            # print(visited)
            return 0 <= i < m and 0 <= j < n and (i, j) not in visited

        queue = []
        queue.append((0, 0, 0))
        visited = {(0, 0)}
        dirs = [(-1,0), (0, -1), (1, 0), (0, 1)]
        possible = False
        while queue:
            # print(queue)
            time,i,j = heappop(queue)
            
            if i == m - 1 and j == n - 1:
                return time
            
            # next_time = time + 1
            for x, y in dirs:
                next_time = time + 1
                if reachable(i + x, j + y, visited):
                    needed = grid[i + x][j + y]
                    
                    if needed > next_time:
                        diff = needed - next_time
                        if diff & 1:
                            next_time = needed + 1
                        else:
                            next_time = needed

                    
                    heappush(queue, (next_time, i + x, j + y))
                    visited.add((i + x, j + y))
                    possible = True

            
