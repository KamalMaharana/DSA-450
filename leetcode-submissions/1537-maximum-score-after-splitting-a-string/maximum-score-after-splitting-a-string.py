class Solution:
    def maxScore(self, s: str) -> int:
        ones = 0
        for i in s:
            if i == "1":
                ones += 1
                
        result = 0
        c0, c1 = 0, 0
        for idx in range(len(s) - 1):
            i = s[idx]
            if i == "0":
                c0 += 1
            else:
                c1 += 1
            right1 = ones - c1
            result = max(c0 + right1, result)
        return result