class Solution:
    def pathExistenceQueries(self, n: int, nums: List[int], maxDiff: int, queries: List[List[int]]) -> List[bool]:
        class DSU:
            def __init__(self, n: int):
                # Every element is initially its own parent. Rank tracks tree height.
                self.parent = list(range(n))
                self.rank = [1] * n

            def find(self, i: int) -> int:
                # Path Compression: Flattens the tree structure on lookup
                if self.parent[i] != i:
                    self.parent[i] = self.find(self.parent[i])
                return self.parent[i]

            def union(self, i: int, j: int) -> bool:
                root_i = self.find(i)
                root_j = self.find(j)
                
                if root_i == root_j:
                    return False  # Already in the same set (detected a cycle)
                    
                # Union by Rank: Attach smaller tree under deeper tree
                if self.rank[root_i] > self.rank[root_j]:
                    self.parent[root_j] = root_i
                elif self.rank[root_i] < self.rank[root_j]:
                    self.parent[root_i] = root_j
                else:
                    self.parent[root_j] = root_i
                    self.rank[root_i] += 1
                    
                return True  # Successfully merged distinct sets
        
        s = DSU(n)
        for i in range(1, len(nums)):
            a = nums[i - 1]
            b = nums[i]
            if b - a <= maxDiff:
                s.union(i - 1, i)
        
        res = []
        for a, b in queries:
            pa = s.find(a)
            pb = s.find(b)
            if pa == pb:
                res.append(True)
            else:
                res.append(False)
        return res