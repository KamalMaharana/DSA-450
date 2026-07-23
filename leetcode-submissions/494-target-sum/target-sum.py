class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        dp = [[0 for j in range(target + 1)] for i in range(len(nums))]
        @cache
        def dfs(i, val):
            if i == len(nums):
                if val == target:
                    return 1
                return 0

            a = dfs(i + 1, val + nums[i])
            b = dfs(i + 1, val - nums[i])
            return a + b

        return dfs(0, 0)
