class Solution:
    def findMatrix(self, nums: List[int]) -> List[List[int]]:
        curr_set = set()
        result = []
        for i in nums:
            found = False
            # print("Start",i)
            for row in result:
                if i not in row:
                    row.append(i)
                    # print(row)
                    found = True
                    break
            if not found:
                result.append([i])
                # print("After row",result)
        return result

