class Solution:
    def mincostToHireWorkers(self, quality: List[int], wage: List[int], k: int) -> float:
        unit_price = sorted([(wage[i] / quality[i], quality[i]) for i in range(len(wage))])

        quantity = 0
        heap = []
        cost = float('inf')

        for price, unit in unit_price:
            quantity += unit
            heapq.heappush(heap, -unit)

            if len(heap) > k: 
                quantity += heapq.heappop(heap)

            if len(heap) == k:
                cost = min(cost, quantity * price)
        
        return cost