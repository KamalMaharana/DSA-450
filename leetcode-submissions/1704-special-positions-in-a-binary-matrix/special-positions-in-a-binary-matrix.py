class Solution:
    def numSpecial(self, matrix: List[List[int]]) -> int:
        rows = [0] * len(matrix)
        cols = [0] * len(matrix[0])
        ones = []
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == 1:
                    rows[i] += 1
                    cols[j] += 1
                    ones.append([i, j])
        
        result = 0
        for i,j in ones:
            if rows[i] == 1 and cols[j] == 1:
                result += 1
        return result