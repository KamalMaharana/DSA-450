class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        nums.sort()
        arr_len = len(nums)
        @cache
        def dfs(prev, curr):
            if curr == arr_len:
                return []
            
            notTaken = []
            notTaken = dfs(prev, curr + 1)

            taken = []
            if prev == -1 or nums[curr] % nums[prev] == 0:
                taken = [nums[curr]] + dfs(curr, curr + 1)
            
            if len(taken) > len(notTaken):
                return taken
            return notTaken
        
        return dfs(-1, 0)


