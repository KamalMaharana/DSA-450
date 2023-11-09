class Solution:
    def countHomogenous(self, s: str) -> int:
        MOD = (10 ** 9) + 7
        substrings = defaultdict(int)
        i = 0
        j = 0
        result = 0
        while i < len(s) and j < len(s):
            while j < len(s) and s[i] == s[j]:
                j += 1
            # print(i, j)
            n = (j - i)
            result += (n * (n + 1))//2
            i = j
        return result % MOD