class Solution:
    def maximumGap(self, skill: str, station: str) -> int:
        l1, l2 = len(skill), len(station)
        i = 0
        l2r = [-1] * l1
        for j in range(l2):
            if i < l1 and station[j] == skill[i]:
                print(i)
                l2r[i] = j
                i += 1
        
        i = l1 - 1
        r2l = [-1] * l1
        for j in range(l2 - 1, -1, -1):
            if i >= 0 and station[j] == skill[i]:
                r2l[i] = j
                i -= 1
        
        # print(l2r, r2l)
        gap = 0
        for i in range(l1 - 1):
            gap = max(gap, r2l[i + 1] - l2r[i])
        return gap