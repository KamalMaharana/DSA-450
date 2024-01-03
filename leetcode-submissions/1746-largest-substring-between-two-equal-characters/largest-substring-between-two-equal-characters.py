class Solution:
    def maxLengthBetweenEqualCharacters(self, s: str) -> int:
        v1 = [-1] * 26
        v2 = [-1] * 26
        ans = -1

        for i in range(len(s)):
            temp = ord(s[i]) - ord('a')

            if v1[temp] == -1:
                v1[temp] = i
            else:
                v2[temp] = i
                ans = max(ans, v2[temp] - v1[temp] - 1)

        return ans

