class Solution:
    def processStr(self, s: str) -> str:
        res = []
        for i in s:
            # print(res)
            if i == "*":
                if res:
                    res.pop()
            elif i == "#":
                res = res + res
            elif i == "%":
                res = res[::-1]
            else:
                res.append(i)
        return "".join(res) if res else ""