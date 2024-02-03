class Solution:
    def maxSumAfterPartitioning(self, arr: List[int], k: int) -> int:
        def dfs(start):
            if start >= n:
                return 0
            
            if start in dp:
                return dp[start]
            
            max_ele = 0
            max_sum = 0
            for i in range(start, min(start + k, n)):
                max_ele = max(max_ele, arr[i])
                max_sum = max(max_sum, max_ele * (i - start + 1) + dfs(i + 1))
            dp[start] = max_sum
            return max_sum
        
        n = len(arr)
        dp = defaultdict(int)
        return dfs(0)
