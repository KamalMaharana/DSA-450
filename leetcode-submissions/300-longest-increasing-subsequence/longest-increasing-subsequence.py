class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        l = len(nums)
        dp = [1 for i in range(l)]
        for i in range(l):
            for j in range(i, l):
                if nums[j] > nums[i] and dp[j] <= dp[i]:
                    dp[j] = 1 + dp[i]
        return max(dp)