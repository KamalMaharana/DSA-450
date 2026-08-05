from collections import defaultdict, deque

class Solution:
    def remainingMethods(self, n: int, k: int, invocations: list[list[int]]) -> list[int]:
        graph = defaultdict(list)
        for u, v in invocations:
            graph[u].append(v)
            
        # Step 1: Find all suspicious methods using BFS/DFS starting from k
        suspicious = set()
        queue = deque([k])
        suspicious.add(k)
        
        while queue:
            node = queue.popleft()
            for neighbor in graph[node]:
                if neighbor not in suspicious:
                    suspicious.add(neighbor)
                    queue.append(neighbor)
                    
        # Step 2: Check if any non-suspicious method invokes a suspicious method
        for u, v in invocations:
            if u not in suspicious and v in suspicious:
                # Removal is invalid; return all methods
                return list(range(n))
                
        # Step 3: If valid, return all methods that are not suspicious
        return [i for i in range(n) if i not in suspicious]