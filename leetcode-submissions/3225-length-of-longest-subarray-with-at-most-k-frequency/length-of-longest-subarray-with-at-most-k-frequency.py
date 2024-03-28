class Solution:
    def maxSubarrayLength(self, nums: List[int], k: int) -> int:
        freq = defaultdict(int)
        left = 0
        right = 0
        curr_max = 0
        res = 0
        while right < len(nums):
            n = nums[right]
            freq[n] += 1
            while freq[n] > k:
                n2 = nums[left]
                freq[n2] -= 1
                left += 1
            res = max(res, right - left + 1)
            right += 1
        return res
