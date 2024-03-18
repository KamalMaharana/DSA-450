class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        n, count = len(points), 1
        if n == 0: return 0
        points.sort()
        curr = points[0]
        
        for i in range(1, n):
            if curr[1] >= points[i][0]:
                curr = [max(curr[0], points[i][0]), min(curr[1], points[i][1])]
            else:
                count += 1
                curr = points[i]
        
        # points.sort(key = lambda x: x[1])
        
        # for i in range(n):
        #     if curr[1] < points[i][0]:
        #         count += 1
        #         curr = points[i]
                
        return count