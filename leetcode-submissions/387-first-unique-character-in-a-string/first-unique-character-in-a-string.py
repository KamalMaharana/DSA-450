class Solution:
    def firstUniqChar(self, s: str) -> int:
        from collections import Counter
        temp = Counter(s)
        for i in s:
            if temp[i] == 1:
                return s.index(i)
        return -1