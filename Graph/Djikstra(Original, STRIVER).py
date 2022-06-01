# Dijkstra Algorithm
from collections import defaultdict
import heapq


class Graph:
    def __init__(self, count):
        self.graph = defaultdict(lambda: defaultdict(lambda: 0))
        self.count = count + 1

    def insert(self, src, dst, wt):
        self.graph[src][dst] = wt

    def dijkstra(self, src: int) -> list:
        distance = [float('inf')] * self.count
        distance[src] = 0
        heap = [[src, 0]]
        heapq.heapify(heap)
        while heap:
            node, dist = heapq.heappop(heap)
            for neighbour in self.graph[node]:
                weight = self.graph[node][neighbour]
                if (distance[node] + weight) < distance[neighbour]:
                    distance[neighbour] = distance[node] + weight
                    heapq.heappush(heap, [neighbour, distance[neighbour]])
        return distance[1:]
        pass

def maximum(arr, index):
    if index == len(arr):
        return float('inf')
    return min(arr[index], maximum(arr, index + 1))

if __name__ == '__main__':
    g = Graph(5)
    g.insert(1, 2, 2)
    g.insert(1, 4, 1)
    g.insert(2, 1, 2)
    g.insert(2, 3, 4)
    g.insert(2, 5, 5)
    g.insert(3, 4, 3)
    g.insert(3, 5, 1)
    g.insert(4, 1, 1)
    g.insert(4, 3, 3)
    g.insert(5, 2, 5)
    g.insert(5, 3, 1)
    print(g.dijkstra(1))
    print(maximum([2,6,1,2,7,8], 0))
