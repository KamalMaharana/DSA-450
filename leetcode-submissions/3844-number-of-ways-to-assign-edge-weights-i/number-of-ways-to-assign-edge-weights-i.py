class Solution:
    def assignEdgeWeights(self, edges: List[List[int]]) -> int:
        MOD = ((10 ** 9) + 7)
        graph = defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
        
        queue = [(1,0)]
        edges = 0
        max_depth = 0
        visited = set()
        while queue:
            node, level = queue.pop(0)
            if node in visited:
                continue
            visited.add(node)
            max_depth = max(max_depth, level)
            for baju_wala in graph[node]:
                if baju_wala not in visited:
                    queue.append((baju_wala, level + 1))
        return (2 ** (max_depth - 1)) % MOD
