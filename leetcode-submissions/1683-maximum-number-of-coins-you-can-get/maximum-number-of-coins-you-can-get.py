class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        piles.sort()
        n = len(piles)
        u,b = n - 2, 0
        result = 0
        while b < u:
            result += piles[u]
            b += 1
            u -= 2
            
        return result