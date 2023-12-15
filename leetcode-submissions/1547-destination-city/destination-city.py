class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        cities = set()
        outgoing = set()
        for i, j in paths:
            cities.add(i)
            cities.add(j)
            outgoing.add(i)
        
        for c in cities:
            if c not in outgoing:
                return c