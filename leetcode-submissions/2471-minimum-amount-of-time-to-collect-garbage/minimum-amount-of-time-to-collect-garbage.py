class Solution:
    def garbageCollection(self, garbage: List[str], travel: List[int]) -> int:
        prefix_sum = []
        prev = 0
        # [2,4,3]
        # [0,2,6,9]
        for i in travel:
            prefix_sum.append(prev)
            prev += i
        prefix_sum.append(prev)
        # print(prefix_sum)
        res = 0
        truck = defaultdict(int)
        for i in range(len(garbage)):
            res += len(garbage[i])
            for c in garbage[i]:
                truck[c] = i
        
        for c in truck:
            index = truck[c]
            res += prefix_sum[index]
        return res
