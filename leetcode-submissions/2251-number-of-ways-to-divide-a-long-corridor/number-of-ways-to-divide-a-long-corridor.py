class Solution:
    def numberOfWays(self, corridor: str) -> int:
        segments = []
        start, end = None, None
        count = 0
        for i, val in enumerate(corridor):
            if val == "S":
                if start is None:
                    start = i
                
                if end is None and start != i:
                    end = i
                    segments.append([start, end])
                    start = None
                    end = None
                count += 1
            
        # print(segments)
        n = len(segments)
        if count % 2 != 0:
            return 0
        if n < 2:
            return n

        result = 1
        for i in range(1, n):
            end1 = segments[i - 1][1]
            start2 = segments[i][0]
            result *= (start2 - end1)
        
        MOD = (10 ** 9)+ 7
        return result % MOD
                