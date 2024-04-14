class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        stack = []
        temp = k
        for i in num:
            while k and stack and stack[-1] > i:
                stack.pop()
                k -= 1
            stack.append(i)
        while k:
            stack.pop()
            k -= 1
        res = "".join(stack)
        res = res.lstrip("0")
        # res = "".join(stack[0:len(num)-temp]).lstrip("0")
        if len(res):
            return res
        return "0"