from collections import Counter
from typing import List

class Solution:
    def maximumLength(self, nums: List[int]) -> int:
        freq = Counter(nums)
        
        # 1. Handle the edge case for '1's upfront
        # If we have an even number of 1s, we can use at most freq[1] - 1 (must be odd)
        if 1 in freq:
            res = freq[1] if freq[1] % 2 != 0 else freq[1] - 1
        else:
            res = 1
            
        # 2. Iterate through other unique values > 1
        # We don't strictly need to sort them because we check all paths completely,
        # but filtering out 1 avoids an infinite loop since 1**2 == 1.
        unique_vals = [val for val in freq if val > 1]
        
        for val in unique_vals:
            current_length = 0
            current_val = val
            
            # Keep building the flanks of the sequence as long as we have 
            # at least 2 copies of the current number and its square exists
            while freq[current_val] >= 2 and (current_val ** 2) in freq:
                current_length += 2
                current_val = current_val ** 2
            
            # The loop breaks when we reach the peak element.
            # A valid peak only requires 1 count to cap off the sequence.
            current_length += 1
            
            # Track the maximum subset length found
            res = max(res, current_length)
            
        return res