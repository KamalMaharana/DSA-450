class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        nums.sort()
        arr_len = len(nums)
        dp = [[[] for _ in range(arr_len + 1)] for _ in range(arr_len + 1)]

        for curr in range(arr_len - 1, -1, -1):
            for prev in range(curr - 1, -2 , -1):
                # Option 1: Skip current element -> mapped from dfs(prev, curr + 1)
                notTaken = dp[prev + 1][curr + 1]

                # Option 2: Take current element -> mapped from dfs(curr, curr + 1)
                taken = []
                if prev == -1 or nums[curr] % nums[prev] == 0:
                    # prev = curr maps to row index (curr + 1) due to the +1 shift
                    taken = [nums[curr]] + dp[curr + 1][curr + 1]

                # Step 4: Record optimal subset for state (prev, curr)
                if len(taken) > len(notTaken):
                    dp[prev + 1][curr] = taken
                else:
                    dp[prev + 1][curr] = notTaken

        # Initial call was dfs(-1, 0) -> maps to dp[-1 + 1][0] = dp[0][0]
        return dp[0][0]