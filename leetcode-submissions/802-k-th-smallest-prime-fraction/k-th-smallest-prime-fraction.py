class Solution:
    def kthSmallestPrimeFraction(self, arr: List[int], k: int) -> List[int]:
        s = []
        for i in arr:
            for j in arr:
                s.append([i/j, i, j])
        s.sort()
        return s[k - 1][1:]