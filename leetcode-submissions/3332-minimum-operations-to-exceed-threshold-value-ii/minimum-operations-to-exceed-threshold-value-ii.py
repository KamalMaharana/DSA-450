class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        heapify(nums)
        heap = nums
        cnt = 0
        while len(heap) >= 2:
            a = heappop(heap)
            b = heappop(heap)
            if a >= k:
                return cnt
            
            val = min(a, b) * 2 + max(a, b)
            heappush(heap, val)
            # print(heap)
            cnt += 1
        return cnt