class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1: return nums[0]
        def dp(arr):
            n = len(arr)
            if n == 1: return arr[0]
            prev = 0
            curr = arr[0]
            res = 0
            for i in range(1, n):
                res = max(curr, arr[i] + prev)
                prev = curr
                curr = res
            return res
        
        res = max(dp(nums[:-1]), dp(nums[1:]))
        return res