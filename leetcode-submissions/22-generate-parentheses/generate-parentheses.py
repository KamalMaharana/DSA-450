class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        # self.res = []
        def dp(o, c, s):
            if o > n or c > n or c > o:
                return
            
            if o == n and c == n:
                res.append(s)
                return
            
            dp(o + 1, c, s + '(')
            dp(o, c + 1, s + ')')
        res = []
        dp(1, 0, '(')
        return res