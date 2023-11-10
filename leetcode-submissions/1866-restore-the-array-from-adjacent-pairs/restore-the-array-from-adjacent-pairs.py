class Solution:
    def restoreArray(self, adjacentPairs: List[List[int]]) -> List[int]:
        graph = defaultdict(list)
        freq = defaultdict(int)
        for u, v in adjacentPairs:
            graph[u].append(v)
            graph[v].append(u)
            freq[u] += 1
            freq[v] += 1
        start = None
        for i in freq:
            if freq[i] == 1:
                start = i
                break
        stack = []
        visited = set()
        def dfs(node):
            if node not in visited:
                visited.add(node)
                for baju_wala in graph[node]:
                    dfs(baju_wala)
                stack.append(node)
        
        dfs(start)
        for i in freq:
            if i not in visited:
                dfs(i)
        
        return stack