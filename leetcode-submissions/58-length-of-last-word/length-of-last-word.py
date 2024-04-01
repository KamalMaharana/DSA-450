class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        s = [i for i in s.split(" ") if i!= ""]
        if len(s) > 0:
            return len(s[-1])
        return 0
        