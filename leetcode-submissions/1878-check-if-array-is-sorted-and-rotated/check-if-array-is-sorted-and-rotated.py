class Solution:
    def check(self, nums: List[int]) -> bool:
        n = len(nums)
        if n == 1:
            return True
        i = 1
        pivot = False
        while i < n:
            while i < n and nums[i] > nums[i - 1]:
                i += 1
            
            if i < n and nums[i] < nums[i - 1]:
                if pivot:
                    return False
                pivot = True
            
            i += 1

        if nums[-1] > nums[0] and pivot:
            return False
        return True
