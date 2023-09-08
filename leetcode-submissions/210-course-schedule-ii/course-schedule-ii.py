class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph = defaultdict(lambda: [])
        for v, u in prerequisites:
            graph[u].append(v)
        # print(graph)
        visited = [0] * numCourses
        stack = []
        self.foundCycle = False
        
        def dfs(node):
            # print(node)
            if self.foundCycle:
                return
            if visited[node] == 1:
                self.foundCycle = True
                return
            if visited[node] == 0:
                visited[node] = 1
                # visited[node] = True
                for neig in graph[node]:
                    dfs(neig)
                visited[node] = 2
                stack.append(node)
        
        
        for i in range(0, numCourses):
            if self.foundCycle: return []
            if visited[i] == 0:
                dfs(i)
        # print(stack)
        # print(self.foundCycle)
        return stack[::-1] if not self.foundCycle else []