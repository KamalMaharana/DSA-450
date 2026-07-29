from collections import Counter

class Solution:
    # Cap combinations to 10^6 + 1 to prevent large integer overflow
    LIMIT = 1_000_001

    def smallestPalindrome(self, s: str, k: int) -> str:
        # Step 1: Extract left half and optional middle character
        half_len = len(s) // 2
        mid = s[half_len] if len(s) % 2 == 1 else ""
        
        # Count frequencies for the left half
        counts = [0] * 26
        for ch in s[:half_len]:
            counts[ord(ch) - ord('a')] += 1

        # Step 2: Validate total possible arrangements >= k
        if self._count_arrangements(counts) < k:
            return ""

        # Step 3: Build the left half character by character
        left = []
        for _ in range(half_len):
            for i in range(26):
                if counts[i] == 0:
                    continue

                # Try placing letter i at the current position
                counts[i] -= 1
                ways = self._count_arrangements(counts)

                if k <= ways:
                    left.append(chr(ord('a') + i))
                    break  # Locked in character i
                else:
                    k -= ways
                    counts[i] += 1  # Backtrack and try next character

        # Step 4: Reconstruct full palindrome
        left_str = "".join(left)
        return left_str + mid + left_str[::-1]

    def _count_arrangements(self, counts: list[int]) -> int:
        """Calculates multiset permutations: C(N, c0) * C(N-c0, c1) * ..."""
        total = sum(counts)
        res = 1
        for freq in counts:
            if freq == 0:
                continue
            res *= self._nCr(total, freq)
            if res >= self.LIMIT:
                return self.LIMIT
            total -= freq
        return res

    def _nCr(self, n: int, r: int) -> int:
        """Calculates combinations nCr capped at LIMIT."""
        r = min(r, n - r)
        res = 1
        for i in range(1, r + 1):
            res = res * (n - i + 1) // i
            if res >= self.LIMIT:
                return self.LIMIT
        return res