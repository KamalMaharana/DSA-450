class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        costs.sort()
        i = 0
        result = 0
        while i < len(costs) and coins > 0:
            if coins - costs[i] < 0:
                break
            coins -= costs[i]
            result += 1
            i += 1
        return result