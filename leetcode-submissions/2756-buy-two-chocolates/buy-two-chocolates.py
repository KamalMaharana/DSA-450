class Solution:
    def buyChoco(self, prices: List[int], money: int) -> int:
        prices.sort()
        curr = prices[0] + prices[1]
        if curr > money:
            return money
        return money - curr