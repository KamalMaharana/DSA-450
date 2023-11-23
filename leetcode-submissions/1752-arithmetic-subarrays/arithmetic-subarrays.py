class Solution:
    def checkArithmeticSubarrays(self, nums: List[int], l: List[int], r: List[int]) -> List[bool]:
        n = len(l)
        result = []
        def isArithmetic(arr):
            n = len(arr)
            if n < 2:
                return True
            
            diff = arr[1] - arr[0]
            for i in range(2, n):
                val = arr[i] - arr[i - 1]
                if val != diff:
                    return False
            return True

        for i in range(n):
            left = l[i]
            right = r[i]
            arr = nums[left:right + 1]
            arr.sort()
            result.append(isArithmetic(arr))
        return result