class DSU:
    def __init__(self, nodes):
        self.parent = {node: node for node in range(nodes + 1)}
        self.rank = {node: 0 for node in range(nodes + 1)}
        self.size = {node: 1 for node in range(nodes + 1)}
        
    def findParent(self, node):
        if self.parent[node] == node:
            return node
        # Path compression
        self.parent[node] = self.findParent(self.parent[node])
        return self.parent[node]
    
    def unionByRank(self, u, v):
        u = self.findParent(u)
        v = self.findParent(v)
        # Attaching lesser rank to higher rank to reduce the size
        if self.rank[u] > self.rank[v]: 
            self.parent[v] = u
        elif self.rank[u] < self.rank[v]:
            self.parent[u] = v
        else: 
            self.parent[v] = u      # Attaching 'v' to 'u'; path compression
            self.rank[v] += 1
    
    def unionBySize(self, u, v):
        ult_p_u = self.findParent(u)
        ult_p_v = self.findParent(v)
        # Ultimate Parent of U = ult_p_u
        # Ultimate Parent of V = ult_p_v
        if ult_p_u == ult_p_v: return
        else:
            if self.size[ult_p_u] < self.size[ult_p_v]:
                self.parent[ult_p_v] = ult_p_u
                self.size[ult_p_u] += self.size[ult_p_v]
            else:
                self.parent[ult_p_u] = ult_p_v
                self.size[ult_p_v] += self.size[ult_p_u]
class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        n = len(accounts)
        d = DSU(n)
        _map = defaultdict(int)
        for i in range(n):
            for j in range(1, len(accounts[i])):
                val = accounts[i][j]
                if val in _map:
                    parent_idx = _map[val]
                    # print(val, i, j, parent_idx)
                    d.unionBySize(parent_idx, i)
                    # _map[val] = i
                else:    
                    _map[val] = i
        
        temp_res = [[] for i in range(n)]
        for k in _map:
            idx = d.findParent(_map[k])
            # print(idx, _map[k], temp_res)
            temp_res[idx].append(k)
        # print(_map)
        # print(d.parent)
        # print(temp_res)
        ans = []
        # print(temp_res)
        for i in range(n):
            if len(temp_res[i]) != 0:
                name = accounts[i][0]
                temp_res[i].sort()
                emails = temp_res[i]
                temp = [name] + emails
                # print(temp)
                ans.append(temp)
        return ans