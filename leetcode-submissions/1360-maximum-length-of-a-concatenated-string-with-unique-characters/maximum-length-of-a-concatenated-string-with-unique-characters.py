class Solution:
        
    def maxLength(self, arr: List[str]) -> int:
        arrNew = []
        for a in arr:
            # Check for unique characters within current string
            if len(a) == len(set(a)):
                arrNew.append(a)
        
        @cache
        def subSequences(index, temp):
            if index == len(arrNew):
                # Check for unique characters within current string
                if len(temp) == len(set(temp)):
                    return len(temp)
                else:
                    return -1
            else:
                return max(
                    subSequences(index + 1, temp + arrNew[index]),
                    subSequences(index + 1, temp))
        return subSequences(0, '')