class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        result = 0
        n = len(s)
        for i in range(26):
            chars = set()
            ch = chr(i + ord('a'))
            i = 0
            j = len(s) - 1
            while i < n:
                if s[i] == ch:
                    break
                i += 1

            while j >= 0:
                if s[j] == ch:
                    break
                j -= 1
            
            for k in range(i + 1, j):
                chars.add(s[k])
            result += len(chars)
        return result