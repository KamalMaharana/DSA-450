class Solution:
    def queryResults(self, limit: int, queries: List[List[int]]) -> List[int]:
        cb = defaultdict(set)
        bc = defaultdict(int)
        res = []
        for ball, clr in queries:
            if ball in bc:
                curr_clr = bc[ball]
                cb[curr_clr].remove(ball)
                if len(cb[curr_clr]) == 0:
                    cb.pop(curr_clr)

            bc[ball] = clr
            cb[clr].add(ball)
            res.append(len(cb))
        return res