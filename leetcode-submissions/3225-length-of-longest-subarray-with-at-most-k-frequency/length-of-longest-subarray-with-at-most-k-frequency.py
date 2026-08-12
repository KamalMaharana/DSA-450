class Solution:
    def maxSubarrayLength(self, nums: List[int], k: int) -> int:
        i = 0
        j = 0
        l = len(nums)
        _map = defaultdict(int)
        res = 0
        while j < l:
            # print(_map)
            n = nums[j]
            while i < j and _map[n] >= k:
                prev = nums[i]
                _map[prev] -= 1
                i += 1
            
            _map[n] += 1            
            res = max(res, j - i + 1)
            j += 1
        return res
        