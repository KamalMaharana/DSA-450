class Solution:
    def missingInteger(self, nums: List[int]) -> int:
        s = set(nums)
        
        # 1. Calculate the sum of the sequential PREFIX (starts at index 0)
        seq_sum = nums[0]
        for i in range(1, len(nums)):
            if nums[i] == nums[i - 1] + 1:
                seq_sum += nums[i]
            else:
                break  # Stop as soon as the prefix breaks!
                
        # 2. Find the smallest integer >= seq_sum that is missing from nums
        while seq_sum in s:
            seq_sum += 1
            
        return seq_sum