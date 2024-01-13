class Solution:
    def minSteps(self, s: str, t: str) -> int:
        freq1 = Counter(s)
        freq2 = Counter(t)
        result = 0
        for ch in freq1:
            if ch not in freq2:
                result += freq1[ch]
            else:
                if freq1[ch] > freq2[ch]:
                    result += (freq1[ch] - freq2[ch])
        return result