class Solution:
    def maximumImportance(self, n: int, roads: List[List[int]]) -> int:
        graph = defaultdict(int)
        for u,v in roads:
            graph[u] += 1
            graph[v] += 1
        
        temp = []
        for k in graph:
            temp.append([graph[k], k])
        
        temp.sort(reverse = True)
        for i, val in enumerate(temp):
            rank = n
            k = val[1]
            graph[k] = rank
            n -= 1
        
        result = 0
        for u, v in roads:
            result += graph[u] + graph[v]
        return result