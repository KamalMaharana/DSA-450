class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        if rowIndex == 0:
            return [1]
        elif rowIndex == 1:
            return [1,1]
        n = 1
        prev = [1,1]
        while n < rowIndex:
            curr = [1]
            for i in range(1, len(prev)):
                curr.append(prev[i - 1] + prev[i])
            curr.append(1)
            prev = curr
            n += 1
        return curr