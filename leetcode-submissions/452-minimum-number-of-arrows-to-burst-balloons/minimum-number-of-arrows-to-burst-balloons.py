class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort()
        merged = []
        for curr_start, curr_end in points:
            if merged:
                prev_start, prev_end = merged[-1]
                if curr_start <= prev_end:
                    new_start = max(curr_start, prev_start)
                    new_end = min(curr_end, prev_end)
                    merged.pop()
                    merged.append([new_start, new_end])
                else:
                    merged.append([curr_start, curr_end])
            else:
                merged.append([curr_start, curr_end])
        # print(merged)
        return len(merged)
