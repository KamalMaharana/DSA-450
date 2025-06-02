class Solution:
    def candy(self, ratings: List[int]) -> int:
        Candies = [1 for i in ratings]
        
        # left Pass; this will allocate more assign more candies if left neighbour has less rating
        for i in range(1, len(ratings)):
            if ratings[i] > ratings[i - 1]:
                Candies[i] = Candies[i - 1] + 1
        
        # Right Pass; this will allocate more assign more candies if right neighbour has less rating
        for i in range(len(ratings) - 1, 0, -1):
            if ratings[i - 1] > ratings[i]:
                Candies[i - 1] = max(Candies[i] + 1, Candies[i - 1])
        
        result = sum(Candies)
        return result
        
        