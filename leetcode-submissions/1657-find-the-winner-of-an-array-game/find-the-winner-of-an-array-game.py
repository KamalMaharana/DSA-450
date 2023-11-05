class Solution:
    def getWinner(self, arr: List[int], k: int) -> int:
        _map = defaultdict(int)
        i = 0
        j = 1
        while i < len(arr) and j < len(arr):
            a = arr[i]
            b = arr[j]
            if a > b:
                _map[a] += 1
                if _map[a] == k:
                    return a
                j += 1
            else:
                _map[b] += 1
                if _map[b] == k:
                    return b
                i = j
                j += 1
        return arr[i]
