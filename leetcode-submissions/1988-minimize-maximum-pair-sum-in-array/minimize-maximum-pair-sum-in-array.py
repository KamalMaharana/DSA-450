class Solution:
    def minPairSum(self, nums: List[int]) -> int:
        nums.sort()
        n = len(nums)
        maxi = 0
        for i in range(n//2):
            start = i
            end = n - i - 1
            maxi = max(nums[start] + nums[end], maxi)
        return maxi
