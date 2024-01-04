class Solution:
    def minOperations(self, nums: List[int]) -> int:
        freq = Counter(nums)
        # print(freq)
        res = 0
        for f in freq.values():
            if f == 1:
                return -1
            res += f // 3
            if f % 3:
                res += 1
            
        return res
            
            