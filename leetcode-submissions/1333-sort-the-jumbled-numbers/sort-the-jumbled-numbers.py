class Solution:
    def sortJumbled(self, mapping: List[int], nums: List[int]) -> List[int]:
        pos = dict()
        for n in nums:
            temp = ""
            for d in str(n):
                temp += str(mapping[int(d)])
            pos[n] = int(temp)
        nums.sort(key = lambda x: pos[x])
        return nums