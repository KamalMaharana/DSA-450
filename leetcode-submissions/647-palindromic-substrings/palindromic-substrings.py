class Solution:
    def countSubstrings(self, s: str) -> int:
        if len(s) == 1:
            return 1
        def expandFromMiddle(s, left, right):
            count = 0
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
                count += 1
            
            return count
        
        res = 0
        l = 0
        for i in range(len(s)):
            count1 = expandFromMiddle(s, i, i)
            count2 = expandFromMiddle(s, i, i+1)
            res += count1 + count2
            
        return res