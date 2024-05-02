class Solution:
    def findMaxK(self, nums: List[int]) -> int:
        freq = Counter(nums)
        res = -1
        for n in freq:
            target = n * -1
            if target in freq:
                res = max(res, target)
        return res