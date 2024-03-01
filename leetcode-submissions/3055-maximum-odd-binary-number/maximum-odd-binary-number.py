class Solution:
    def maximumOddBinaryNumber(self, s: str) -> str:
        ones = 0
        for i in s:
            if i == "1":
                ones += 1
        
        ones -= 1
        res = ""
        print(ones)
        while len(res) < len(s) - 1:
            while ones:
                res += "1"
                ones -= 1
            if len(res) == len(s) - 1:
                res += "1"
            else:
                res += "0"
        
        if len(res) == len(s) - 1:
            res += "1"
        return res