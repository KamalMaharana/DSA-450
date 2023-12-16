class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        freq_s = Counter(s)
        freq_t = Counter(t)
        for i in freq_s:
            if i not in freq_t:
                return False
            if freq_s[i] != freq_t[i]:
                return False
        for i in freq_t:
            if i not in freq_s:
                return False
            if freq_s[i] != freq_s[i]:
                return False
        return True
        