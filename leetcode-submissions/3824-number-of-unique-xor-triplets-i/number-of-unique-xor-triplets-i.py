class Solution:
    def uniqueXorTriplets(self, nums: List[int]) -> int:
        n = len(nums)
        if n <= 2:
            return n
        
        k = 0
        while n > 0:
            n = n >> 1
            k += 1
        return 2 ** k