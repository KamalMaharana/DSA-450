class Solution:
    def firstStableIndex(self, nums: list[int], k: int) -> int:
        n = len(nums)
        minis = [-1] * n
        maxs = [-1] * n
        maxs[0] = nums[0]
        minis[-1] = nums[-1]
        for i in range(1, n):
            maxs[i] = max(maxs[i - 1], nums[i])
        for i in range(n - 2, -1, -1):
            minis[i] = min(minis[i + 1], nums[i])
        
        for i in range(n):
            if maxs[i] - minis[i] <= k:
                return i
        return -1