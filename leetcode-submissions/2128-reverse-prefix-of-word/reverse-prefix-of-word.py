class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        n = len(word)
        for i in range(n):
            w = word[i]
            if w == ch:
                temp = word[0:i+1]
                temp = temp[::-1]
                return temp + word[i+1:]
        return word