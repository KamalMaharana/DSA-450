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
        def dfs(u):
            stack.append(u)
            visited.add(u)
            for v in graph[u]:
                if v not in visited:
                    dfs(v)
        
        dfs(start)
        # for i in freq:
        #     if i not in visited:
        #         dfs(i)
        
        return stack