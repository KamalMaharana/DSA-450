class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return nums[0]
        curr = nums[0]
        prev = 0
        res = 0
        for i in range(1, n):
            res = max(curr, nums[i] + prev)
            prev = curr
            curr = res
        return res