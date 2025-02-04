class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        start = 0
        end = 0
        maxi = nums[0]
        curr = nums[0]
        for i in range(1,len(nums)):
            if nums[i] > nums[i - 1]:
                end = i
                curr += nums[i]
            else:
                start = i
                end = i
                curr = nums[i]
            maxi = max(maxi, curr)
        return maxi