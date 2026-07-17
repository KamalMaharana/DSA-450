import math
from typing import List
from bisect import bisect_right

class Solution:
    def gcdValues(self, nums: List[int], queries: List[int]) -> List[int]:
        max_val = max(nums)
        
        # 1. Count frequencies of each number
        counts = [0] * (max_val + 1)
        for x in nums:
            counts[x] += 1
            
        # 2. Calculate exact GCD pairs working backward
        gcd_pairs = [0] * (max_val + 1)
        
        for g in range(max_val, 0, -1):
            # Count how many total numbers are multiples of g
            total_multiples = 0
            for multiple in range(g, max_val + 1, g):
                total_multiples += counts[multiple]
                
            # Total combinations of pairs we can make from these multiples
            total_pairs = (total_multiples * (total_multiples - 1)) // 2
            
            # Subtract pairs that actually have a HIGHER greatest common divisor
            for multiple in range(2 * g, max_val + 1, g):
                total_pairs -= gcd_pairs[multiple]
                
            gcd_pairs[g] = total_pairs
            
        # 3. Create a running total (Prefix Sum) of the pairs
        prefix_sums = [0] * (max_val + 1)
        for i in range(1, max_val + 1):
            prefix_sums[i] = prefix_sums[i - 1] + gcd_pairs[i]
            
        # 4. Answer queries instantly using Binary Search
        res = []
        for q in queries:
            # We look for the first bucket where the running total is strictly greater than q
            idx = bisect_right(prefix_sums, q)
            res.append(idx)
            
        return res