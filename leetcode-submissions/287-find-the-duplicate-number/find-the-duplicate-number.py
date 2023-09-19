class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        i = 0
        while i < len(nums):
            # print(nums, i)
            index = abs(nums[i]) - 1
            # print(index)
            if nums[index] < 0:
                return index + 1
            nums[index] *= -1
            i += 1
        return -1