class Solution:
    def validPartition(self, nums: List[int]) -> bool:
        dp = dict()
        n = len(nums)
        def dfs(index):
            # print(index)
            if index == n:
                return True
            
            if index in dp: 
                return dp[index]
            twoIdentical = False
            threeIdentical = False
            increasingSeq = False

            if (index < n and index + 1 < n and nums[index] == nums[index + 1]):
                twoIdentical = dfs(index + 2)
            
            if (index < n and index + 1 < n and index + 2 < n and nums[index] == nums[index + 1] == nums[index + 2]):
                threeIdentical = dfs(index + 3)
            
            if (index < n and index + 1 < n and index + 2 < n and nums[index] == nums[index + 1] - 1 and nums[index + 1] == nums[index + 2] - 1):
                increasingSeq = dfs(index + 3)
            
            dp[index] = twoIdentical or threeIdentical or increasingSeq
            return dp[index]
        
        return dfs(0)
