class Solution:
    def nthSuperUglyNumber(self, n: int, primes: list[int]) -> int:
        k = len(primes)
        ugly = [1] * n
        idx = [0] * k  # Tracks index in `ugly` array for each prime
        
        for i in range(1, n):
            # Calculate next candidate for each prime using ugly numbers array
            candidates = [primes[j] * ugly[idx[j]] for j in range(k)]
            
            # Pick the smallest candidate
            next_ugly = min(candidates)
            ugly[i] = next_ugly
            
            # Only advance pointer for prime(s) that produced this minimum
            for j in range(k):
                if candidates[j] == next_ugly:
                    idx[j] += 1
                    
        return ugly[-1]