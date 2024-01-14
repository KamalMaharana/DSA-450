class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        if len(word1) != len(word2):
            return False
        f1 = Counter(word1)
        f2 = Counter(word2)
        freq1 = {}
        freq2 = {}
        for i in f1:
            if f1[i] in freq1:
                freq1[f1[i]] += 1
            else:
                freq1[f1[i]] = 1
        for i in f2:
            if f2[i] in freq2:
                freq2[f2[i]] += 1
            else:
                freq2[f2[i]] = 1
        
        for i in f1:
            if i not in f2:
                return False
        for i in freq1:
            if i not in freq2 or freq1[i] != freq2[i]:
                return False
        return True