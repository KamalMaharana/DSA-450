class Solution:
    def reductionOperations(self, nums: List[int]) -> int:
        freq = Counter(nums)
        heap = []
        for i in freq:
            heap.append(-i)
        heap.sort()
        # heap = temp
        res = 0
        # print(heap)
        while len(heap) > 1:
            a = heapq.heappop(heap) * -1
            b = heapq.heappop(heap) * -1
            
            res += freq[a]
            freq[b] += freq[a]
            heapq.heappush(heap, b * -1)
        return res