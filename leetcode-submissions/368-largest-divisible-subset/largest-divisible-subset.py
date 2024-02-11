class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        if not nums: return []
        nums.sort()
        lis = [1] * len(nums)
        previous_index = [-1] * len(nums) # For reverse traversing to form the output array
        max_index = 0
        for i in range(1, len(nums)):
            for j in range(i):
                if nums[i] % nums[j] == 0 and lis[i] < lis[j] + 1:
                    lis[i] = lis[j] + 1
                    previous_index[i] = j
            
            if lis[i] > lis[max_index]:
                max_index = i
        
        # print(lis, max_index, previous_index)
        result = []
        t = max_index
        while t >= 0:
            result.append(nums[t])
            t = previous_index[t]
        
        return result
        