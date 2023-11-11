class Graph:
    def __init__(self, n: int, edges: List[List[int]]):
        self.graph = defaultdict(list)
        self.nodes = n
        for u, v, cost in edges:
            self.graph[u] += [(v, cost)]

    def addEdge(self, edge: List[int]) -> None:
        u, v, cost = edge
        self.graph[u] += [(v, cost)]
        self.nodes += 1
        
    def shortestPath(self, node1: int, node2: int) -> int:
        heap = []
        heappush(heap, (0, node1))
        dist = [inf] * self.nodes
        dist[node1] = 0
        while heap:
            cost, node = heappop(heap)
            if node == node2:
                return cost
            if cost > dist[node]:
                continue

            for baju_wala, new_cost in self.graph[node]:
                new_cost = cost + new_cost
                if new_cost < dist[baju_wala]:
                    dist[baju_wala] = new_cost
                    heappush(heap, (new_cost, baju_wala))
        return -1

# Your Graph object will be instantiated and called as such:
# obj = Graph(n, edges)
# obj.addEdge(edge)
# param_2 = obj.shortestPath(node1,node2)