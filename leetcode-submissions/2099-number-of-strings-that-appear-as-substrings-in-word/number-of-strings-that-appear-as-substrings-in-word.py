class Solution:
    def numOfStrings(self, patterns: List[str], word: str) -> int:
        substrings = set()
        for i in range(len(word)):
            for j in range(i + 1, len(word) + 1):
                substrings.add(word[i:j])
        cnt = 0
        for p in patterns:
            if p in substrings:
                cnt += 1
        return cnt