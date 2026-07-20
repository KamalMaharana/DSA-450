from typing import List

class Solution:
    def minCost(self, n: int, cuts: List[int]) -> int:
        # 1. Add boundaries and sort to easily define intervals
        cuts = [0] + sorted(cuts) + [n]
        m = len(cuts)
        
        # 2. Memoization table
        memo = {}
        
        def dfs(i: int, j: int) -> int:
            # Base Case: No cuts can be made between adjacent indices
            if j - i <= 1:
                return 0
                
            state = (i, j)
            if state in memo:
                return memo[state]
            
            # The cost to make any cut in this interval is the length of the current stick segment
            current_stick_length = cuts[j] - cuts[i]
            
            min_cost = float('inf')
            
            # Try every possible cut 'k' inside the interval (i, j) to see which is best as the last cut
            for k in range(i + 1, j):
                cost = current_stick_length + dfs(i, k) + dfs(k, j)
                if cost < min_cost:
                    min_cost = cost
                    
            memo[state] = min_cost
            return min_cost
            
        return dfs(0, m - 1)