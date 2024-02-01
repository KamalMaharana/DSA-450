class Solution:
    def divideArray(self, nums: List[int], k: int) -> List[List[int]]:
        nums.sort()
        result = []
        prev = nums[0]
        temp = [prev]
        i = 1
        while i < len(nums):
            curr = nums[i]
            diff = curr - prev
            # print(prev, curr, diff)
            if diff > k:
                return []
            temp.append(curr)
            if len(temp) == 3:
                result.append(temp)
                temp = []
                if i + 1 < len(nums):
                    prev = nums[i + 1]
            i += 1

            
        return result