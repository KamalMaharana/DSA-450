class Solution:
    def processStr(self, s: str, k: int) -> str:
        n = len(s)
        lengths = [0] * n
        curr_len = 0
        
        # Step 1: Forward pass to compute lengths after each operation
        for i, char in enumerate(s):
            if char.isalpha():
                curr_len += 1
            elif char == '*':
                curr_len = max(0, curr_len - 1)
            elif char == '#':
                curr_len *= 2
            elif char == '%':
                pass # Length doesn't change on reverse
            lengths[i] = curr_len
            
        # If k is out of bounds of the final string
        if k >= curr_len or k < 0:
            return '.'
            
        # Step 2: Backward pass to trace the origin of index k
        for i in range(n - 1, -1, -1):
            char = s[i]
            prior_len = lengths[i - 1] if i > 0 else 0
            
            if char.isalpha():
                # If k is pointing to the newly added character
                if k == prior_len:
                    return char
                # Otherwise, it belongs to the prefix string before this character
                # k remains the same, stepping back to check previous operations
                
            elif char == '*':
                # The deleted character doesn't contain our target k because
                # we already verified k is within the final valid bounds.
                pass
                
            elif char == '#':
                # If k is in the duplicated second half, wrap it back to the first half
                if k >= prior_len:
                    k %= prior_len
                    
            elif char == '%':
                # Mirror the index across the midpoint of the string
                k = prior_len - 1 - k
                
        return '.'