class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        temp = dict()
        res = []
        for i in strs:
            s = "".join(sorted(i))
            if(s not in temp):
                temp[s] = [i]
            else:
                temp[s].append(i)
        for i in temp:
            res.append(temp[i])
            
        return res