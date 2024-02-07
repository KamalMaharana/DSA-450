class Solution:
    def frequencySort(self, s: str) -> str:
        freq = dict(Counter(s))
        arr = list(zip(freq.keys(), freq.values()))
        arr.sort(key = lambda x: x[1], reverse = True)
        result = ""
        for i in arr:
            result += i[0] * i[1]
        return result
        