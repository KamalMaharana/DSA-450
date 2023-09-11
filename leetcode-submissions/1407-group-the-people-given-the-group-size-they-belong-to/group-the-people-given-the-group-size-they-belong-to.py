class Solution:
    def groupThePeople(self, groupSizes: List[int]) -> List[List[int]]:
        group_map = defaultdict(list)
        for i, val in enumerate(groupSizes):
            group_map[val].append(i)
        
        # print(group_map)
        result = []
        for groupsize in group_map:
            temp = []
            for val in group_map[groupsize]:
                if len(temp) < groupsize:
                    temp.append(val)
                else:
                    result.append(temp)
                    temp = [val]
            
            result.append(temp)
        return result