class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        start1 = intervals[0][0]
        end1 = intervals[0][1]
        result = []
        for i in range(1, len(intervals)):
            start2, end2 = intervals[i][0], intervals[i][1]
            if end1 >= start2:
                start1 = min(start1, start2)
                end1 = max(end1, end2)
            else:
                result.append([start1, end1])
                start1 = start2
                end1 = end2
        result.append([start1, end1])
        return result