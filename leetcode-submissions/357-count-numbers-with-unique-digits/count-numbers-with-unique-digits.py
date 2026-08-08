class Solution:
    def countNumbersWithUniqueDigits(self, n: int) -> int:
        if n == 0:
            return 1
            
        n = min(n, 10)  # Capped at 10 due to Pigeonhole Principle
        
        ans = 10  # Base case for n = 1 (includes 0..9)
        current_options = 9
        available_digits = 9
        
        for k in range(2, n + 1):
            current_options *= available_digits
            ans += current_options
            available_digits -= 1
            
        return ans