class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        result = [[1]]
        if numRows == 1:
            return result
        result.append([1,1])
        for i in range(2, numRows):
            temp = [1]
            prev = result[i - 1]
            # print(prev)
            for j in range(1,len(prev)):
                temp.append(prev[j - 1] + prev[j])
            temp.append(1)
            result.append(temp)
        return result

