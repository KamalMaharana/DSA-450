class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        self.result = 0
        dp = dict()
        def dfs(curr_sum):
            if curr_sum == target:
                dp[curr_sum] = 1
                return 1
            if curr_sum in dp:
                return dp[curr_sum]

            result = 0
            for n in nums:
                if curr_sum + n <= target:
                    result += dfs(curr_sum + n)
            dp[curr_sum] = result
            return result
        self.result = dfs(0)
        return self.result
