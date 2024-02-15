class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        nums.sort()
        sum_val = 0
        ans = -1
        
        for num in nums:
            if num < sum_val:
                ans = num + sum_val
            sum_val += num
            
        return ans