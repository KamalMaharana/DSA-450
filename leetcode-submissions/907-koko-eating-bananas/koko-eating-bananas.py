class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def isPossible(speed):
            count = 0
            for i in piles:
                count += ceil(i/speed)
            return count <= h

        low = 1
        high = max(piles)
        result = high
        while low <= high:
            mid = (low + high) // 2
            # print(low, high)
            if isPossible(mid):
                result = min(result, mid)
                high = mid - 1
            else:
                low = mid + 1
        return result