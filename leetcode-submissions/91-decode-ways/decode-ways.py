class Solution:
    def numDecodings(self, s: str) -> int:
        dp = [0 for i in range(len(s) + 1)]
        if s[0] == "0":
            return 0
        dp[0] = 1
        dp[1] = 1
        for i in range(2, len(s) + 1):
            one = int(s[i - 1])
            two = int(s[i-2] + s[i-1])
            if one >= 1:
                dp[i] += dp[i-1]
            if two >= 10 and two <= 26:
                dp[i] += dp[i-2]
        # print(dp)
        return dp[len(s)]