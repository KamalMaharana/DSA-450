class Solution:
    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
        freq = Counter(arr)
        freq_arr = []
        for key in freq:
            freq_arr.append((freq[key], key))
        freq_arr.sort()
        for i in range(len(freq_arr)):
            temp = freq_arr[i][0]
            while k and temp:
                k -= 1
                temp -= 1
            if k == 0:
                if temp == 0:
                    return len(freq_arr) - (i + 1)
                return len(freq_arr) - i
        return 0