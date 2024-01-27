class Solution:
    def kInversePairs(self, n: int, k: int) -> int:
        MOD = 10**9 + 7
        @cache
        def dp(n, k):
            if k == 0:
                # there is exactly one way to arrange the array (in increasing order)
                return 1
            if k < 0:
                # k in negative area - ivalid
                return 0
            if n == 1:
                # can't create any (k) pairs if array has only 1 element
                return 0
            
            return (dp(n - 1, k) + dp(n, k - 1) - dp(n - 1, k - n)) % MOD
        return dp(n, k)