class Solution:
    def sumAndMultiply(self, s: str, queries: list[list[int]]) -> list[int]:
        n = len(s)
        MOD = 10**9 + 7
        
        # 1. Precompute powers of 10 to extract substrings in O(1) time later
        powers_of_10 = [1] * (n + 1)
        for i in range(1, n + 1):
            powers_of_10[i] = (powers_of_10[i - 1] * 10) % MOD
            
        # 2. Allocate prefix arrays (sized n + 1 to handle 1-based indexing easily)
        digit_sums = [0] * (n + 1)
        nonzero_counts = [0] * (n + 1)
        concatenated_prefix = [0] * (n + 1)
        
        # 3. Fill prefix arrays
        for i, char in enumerate(s, 1):
            digit = int(char)
            
            # Keep track of standard digit sums
            digit_sums[i] = digit_sums[i - 1] + digit
            
            if digit > 0:
                nonzero_counts[i] = nonzero_counts[i - 1] + 1
                # Append the non-zero digit to the running base-10 number
                concatenated_prefix[i] = (concatenated_prefix[i - 1] * 10 + digit) % MOD
            else:
                nonzero_counts[i] = nonzero_counts[i - 1]
                concatenated_prefix[i] = concatenated_prefix[i - 1]
        

        print(concatenated_prefix)
        # 4. Process each query in O(1) constant time
        results = []
        for l, r in queries:
            # Calculate total non-zero digits and their sum in the range [l, r]
            num_nonzero = nonzero_counts[r + 1] - nonzero_counts[l]
            current_sum = digit_sums[r + 1] - digit_sums[l]
            
            # Math Formula: Strip away the prefix before index 'l'
            # (Adding MOD ensures the number never goes negative during subtraction)
            x = (concatenated_prefix[r + 1] - concatenated_prefix[l] * powers_of_10[num_nonzero]) % MOD
            
            results.append((x * current_sum) % MOD)
            
        return results