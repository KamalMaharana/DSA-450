class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], minutes: int) -> int:
        n = len(customers)
        curr_sum = 0
        
        # Calculate baseline satisfied customers and zero out those entries
        for i in range(n):
            if grumpy[i] == 0:
                curr_sum += customers[i]
                customers[i] = 0
        
        # Find maximum additional customers using a sliding window
        window_sum = 0
        max_extra = 0
        
        for i in range(n):
            window_sum += customers[i]
            
            # When the window exceeds 'minutes', slide left pointer
            if i >= minutes:
                window_sum -= customers[i - minutes]
                
            max_extra = max(max_extra, window_sum)
            
        return curr_sum + max_extra