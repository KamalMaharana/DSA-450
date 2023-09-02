class Solution:
    def minimumRounds(self, tasks: List[int]) -> int:
        # any number except 1 can be formed by using 2, 3
        def getCount(n):
            if n%3:
                return n//3 + 1
            return n//3

        freq = Counter(tasks)
        res = 0
        for f in freq:
            if freq[f] == 1:
                return -1
            res += getCount(freq[f])
        return res