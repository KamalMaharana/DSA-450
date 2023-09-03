class Solution:
    def maxHistogram(self, heights):
        def getLeftMinArray(heights):
            n = len(heights)
            minArray = [0] * n
            stack = [] # It will store INDEXES; not Values
            for i in range(n):
                curr_height = int(heights[i])
                while stack and curr_height <= int(heights[stack[-1]]):
                    stack.pop()
                
                if stack:
                    minArray[i] = stack[-1] + 1
                else:
                    minArray[i] = 0
                
                
                stack.append(i)
            return minArray
        def getRightMinArray(heights):
            n = len(heights)
            minArray = [0] * n
            stack = [] # It will store INDEXES; not Values
            for i in range(n - 1, -1, -1):
                curr_height = int(heights[i])
                while stack and curr_height <= int(heights[stack[-1]]):
                    stack.pop()
                
                if stack:
                    minArray[i] = stack[-1] - 1
                else:
                    minArray[i] = n - 1
                
                
                stack.append(i)
            return minArray
        
        leftMinArray = getLeftMinArray(heights)
        rightMinArray = getRightMinArray(heights)
        result = 0
        for i in range(len(heights)):
            width = rightMinArray[i] - leftMinArray[i] + 1
            height = int(heights[i])
            area = width * height
            result = max(result, width * height)
        return result
            
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        if not matrix or len(matrix) == 0:
            return 0
        
        height = matrix[0]
        result = self.maxHistogram(height)
        for i in range(1, len(matrix)):
            prev_height = height
            for j in range(len(matrix[0])):
                if matrix[i][j] != 0 and matrix[i][j] != "0":
                    matrix[i][j] = int(prev_height[j]) + 1
                else:
                    matrix[i][j] = 0
            
            height = matrix[i]
            result = max(result, self.maxHistogram(height))
        
        return result
        
        
        
        
        
        
        
        