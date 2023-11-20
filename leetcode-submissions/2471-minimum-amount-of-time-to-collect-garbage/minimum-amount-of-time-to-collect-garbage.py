class Solution:
    def garbageCollection(self, garbage: List[str], travel: List[int]) -> int:
        prefix_sum = []
        prev = 0
        for i in travel:
            prefix_sum.append(prev)
            prev += i
        prefix_sum.append(prev)
        res = 0
        truck = [0] * 3
        for i in range(len(garbage)):
            res += len(garbage[i])
            for c in garbage[i]:
                if c == "M":
                    truck[0] = i
                elif c == "P":
                    truck[1] = i
                else:
                    truck[2] = i
        for i in range(len(truck)):
            index = truck[i]
            res += prefix_sum[index]
        return res
