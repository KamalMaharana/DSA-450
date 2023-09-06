class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        res, i = [], -1
        I = newInterval
        for i, (x, y) in enumerate(intervals):
            if y < I[0]:
                res.append([x, y])
            elif I[1] < x:
                i -= 1
                break
            else:
                I[0] = min(I[0], x)
                I[1] = max(I[1], y)
                
        return res + [I] + intervals[i+1:]
        