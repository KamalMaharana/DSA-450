class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()
        j = 0
        count = 0
        for req in g:
            while j < len(s) and s[j] < req:
                j += 1
            
            if j < len(s) and s[j] >= req:
                # print(j, req)
                count += 1
                j += 1
        return count