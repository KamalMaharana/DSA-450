class Solution:
    def sortVowels(self, s: str) -> str:
        def isvowel(c):
            return c in {'a','e','i', 'o', 'u'}
        result = []
        vowel = []
        for c in s:
            if isvowel(c.lower()):
                vowel.append(c)
        
        vowel.sort(key= lambda x: ord(x))
        i = 0
        for c in s:
            if isvowel(c.lower()):
                result += vowel[i]
                i += 1
            else:
                result += c
        return "".join(result)