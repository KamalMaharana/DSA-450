class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        left = 0
        right = len(nums) - 1
        n = right + 1
        while left < right:
            mid = (left + right)//2
            if mid > 0 and mid < n - 1:
                if nums[mid-1] < nums[mid] > nums[mid + 1]:
                    return mid
                elif nums[mid + 1] > nums[mid]:
                    left = mid + 1
                else:
                    right = mid - 1
            elif mid == 0:
                if nums[mid] > nums[mid + 1]:
                    return mid
                else:
                    return mid + 1
            elif mid == n - 1:
                if nums[mid] > nums[mid - 1]:
                    return mid
                else:
                    return mid - 1
        return left