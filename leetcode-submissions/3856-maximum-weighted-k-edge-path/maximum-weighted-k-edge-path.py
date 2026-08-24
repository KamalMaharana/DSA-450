class Solution:
    def maxWeight(self, n: int, edges: List[List[int]], k: int, t: int) -> int:
        graph = defaultdict(dict)

        for u, v, w in edges:
            graph[u][v] = w
        
        @cache
        def dfs(node, edges, sums):
            if edges > k or sums >= t:
                return -1
            
            if edges == k:
                return sums

            res = -1
            for v in graph[node]:
                w = graph[node][v]
                res = max(dfs(v, edges + 1, sums + w), res)
            return res

        res = -1
        for node in range(n):
            res = max(res, dfs(node, 0, 0))
        return res