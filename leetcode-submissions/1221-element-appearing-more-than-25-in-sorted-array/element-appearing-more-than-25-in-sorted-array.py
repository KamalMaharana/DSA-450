class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:
        limit = (len(arr) * 25)//100
        # print(limit, len(arr))
        prev = arr[0]
        count = 1
        for i in range(1, len(arr)):
            if arr[i] == prev:
                count += 1
            else:
                prev = arr[i]
                count = 1

            if count > limit:
                return arr[i]
        
        if count > limit:
            return prev
            
