class Solution:
    def countCommas(self, n: int) -> int:
        total_commas = 0
        length = len(str(n))
        
        # Add commas for all full blocks of smaller digit lengths
        # 4-digit numbers start at 10^3, 7-digit at 10^6, etc.
        for digits in range(4, length + 1):
            start = 10 ** (digits - 1)
            # End is either the maximum number with current 'digits' or n, whichever is smaller
            end = min(n, 10 ** digits - 1)
            
            if start <= end:
                count_per_number = (digits - 1) // 3
                total_commas += (end - start + 1) * count_per_number
                
        return total_commas