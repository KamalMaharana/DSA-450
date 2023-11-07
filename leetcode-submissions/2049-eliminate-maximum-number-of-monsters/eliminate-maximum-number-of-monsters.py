class Solution:
    def eliminateMaximum(self, dist: List[int], speed: List[int]) -> int:
        time_taken = []
        n = len(dist)
        for i in range(n):
            if dist[i] < speed[i]:
                time = 1
            else:
                time = ceil(dist[i] / speed[i])
            time_taken.append(time)
        # print(time_taken)
        curr = 0
        time_taken.sort()
        count = 0
        for t in time_taken:
            if t <= curr:
                return count
            curr += 1
            count += 1
        return count


                
