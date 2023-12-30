class Solution:
    def makeEqual(self, words: List[str]) -> bool:
        if len(words) <= 1:
            return True
        freq = defaultdict(int)
        for w in words:
            for ch in w:
                freq[ch] += 1
        # print(freq)
        target = len(words)
        for f in freq:
            if freq[f] % target != 0:
                return False
        return True
