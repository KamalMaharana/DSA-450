class Solution:
    def knightDialer(self, n: int) -> int:
        graph = {0: [4, 6], 1: [6, 8], 2: [9, 7], 3: [4, 8], 4: [3,9,0], 5: [], 6: [1, 7, 0], 7: [2, 6], 
        8: [1, 3], 9: [2, 4]}

        # visited = set()
        dp = defaultdict()
        self.res = 0
        def dfs(n, num):
            if n == 0:
                return 1

            if (n, num) in dp:
                return dp[(n, num)]

            res = 0 
            for baju_wala in graph[num]:
                res += dfs(n - 1, baju_wala)
            dp[(n, num)] = res
            return res
        
        res = 0
        for i in range(10):
            res += dfs(n - 1, i)
            
        MOD = (10 ** 9) + 7
        return res % MOD