class Solution:
    def makeConnected(self, n: int, connections: List[List[int]]) -> int:
        graph = defaultdict(list)
        for u, v in connections:
            graph[u].append(v)
            graph[v].append(u)
        
        visited = set()
        def dfs(node):
            if node in visited:
                return
            
            visited.add(node)
            for neigh in graph[node]:
                dfs(neigh)
        
        count = 0
        for i in range(n):
            if i not in visited:
                count += 1
                dfs(i)
        
        return count - 1 if len(connections) >= n - 1 else -1
