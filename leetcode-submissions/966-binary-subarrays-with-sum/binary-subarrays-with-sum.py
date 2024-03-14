class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        freq = defaultdict(lambda: 0)
        sums = 0
        result = 0
        k = goal
        for i in nums:
            sums += i
            if sums == k:
                result += 1
            
            target = sums - k
            if target in freq:
                result += freq[target]
            
            freq[sums] += 1
        return result