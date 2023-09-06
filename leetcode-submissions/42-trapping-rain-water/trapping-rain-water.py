class Solution:
    def trap(self, height: List[int]) -> int:
        leftmax = 0
        rightmax = 0
        l = 0
        r = len(height) - 1
        result = 0
        while l < r:
            if height[l] <= height[r]:
                if leftmax >= height[l]:
                    result += leftmax - height[l]
                else:
                    leftmax = height[l]
                l += 1
            else:
                if rightmax >= height[r]:
                    result += rightmax - height[r]
                else:
                    rightmax = height[r]
                r -= 1
        return result