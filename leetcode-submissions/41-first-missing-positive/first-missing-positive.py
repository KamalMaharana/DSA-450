class Solution:
    def firstMissingPositive(self, nums: list[int]) -> int:
        n = len(nums)
        
        # Step 1: Put each number in its right place (Cyclic Sort)
        for i in range(n):
            # Keep swapping while current number is valid and not in place
            while 1 <= nums[i] <= n and nums[nums[i] - 1] != nums[i]:
                correct_idx = nums[i] - 1
                nums[i], nums[correct_idx] = nums[correct_idx], nums[i]
                
        # Step 2: Find the first index where nums[i] != i + 1
        for i in range(n):
            if nums[i] != i + 1:
                return i + 1
                
        # Step 3: If 1..N are all present, missing is N + 1
        return n + 1