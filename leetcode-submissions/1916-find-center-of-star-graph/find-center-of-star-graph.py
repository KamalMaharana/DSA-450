class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        graph = defaultdict(list)
        for u,v in edges:
            graph[u].append(v)
            graph[v].append(u)
        
        n = len(graph)
        for k in graph:
            if len(graph[k]) == n - 1:
                return k