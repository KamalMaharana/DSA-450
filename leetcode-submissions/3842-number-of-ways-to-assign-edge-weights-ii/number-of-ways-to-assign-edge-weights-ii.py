from collections import defaultdict, deque
from typing import List

class Solution:
    def assignEdgeWeights(self, edges: List[List[int]], queries: List[List[int]]) -> List[int]:
        MOD = 10**9 + 7
        n = len(edges) + 1
        
        # 1. Build the adjacency list
        graph = defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
            
        # 2. Precompute depths and immediate parents using an iterative DFS
        # up[u][j] will store the (2^j)-th ancestor of node u
        LOG = 17  # Since N <= 10^5, 2^16 = 65536, 2^17 = 131072
        up = [[0] * LOG for _ in range(n + 1)]
        depth = [0] * (n + 1)
        
        # Iterative DFS to avoid Python recursion depth limits
        stack = [1]
        visited = {1}
        depth[1] = 0
        
        while stack:
            curr = stack.pop()
            for neighbor in graph[curr]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    depth[neighbor] = depth[curr] + 1
                    up[neighbor][0] = curr  # 2^0 ancestor is the direct parent
                    stack.append(neighbor)
                    
        # 3. Fill the binary lifting table
        for j in range(1, LOG):
            for i in range(1, n + 1):
                if up[i][j-1] != 0:
                    up[i][j] = up[up[i][j-1]][j-1]
                    
        # Helper function to find the distance between u and v using LCA
        def get_distance(u, v):
            if u == v:
                return 0
                
            original_u, original_v = u, v
            
            # Bring both nodes to the same depth
            if depth[u] < depth[v]:
                u, v = v, u
                
            diff = depth[u] - depth[v]
            for j in range(LOG):
                if (diff >> j) & 1:
                    u = up[u][j]
                    
            if u == v:
                return depth[original_u] + depth[original_v] - 2 * depth[u]
                
            # Lift both nodes together until they are just below their LCA
            for j in range(LOG - 1, -1, -1):
                if up[u][j] != up[v][j]:
                    u = up[u][j]
                    v = up[v][j]
                    
            lca = up[u][0]
            return depth[original_u] + depth[original_v] - 2 * depth[lca]

        # 4. Process all queries efficiently
        res = []
        for u, v in queries:
            k = get_distance(u, v)
            if k == 0:
                res.append(0)
            else:
                # Math insight: 2^(k-1) ways to get an odd sum from k edges
                res.append(pow(2, k - 1, MOD))
                
        return res