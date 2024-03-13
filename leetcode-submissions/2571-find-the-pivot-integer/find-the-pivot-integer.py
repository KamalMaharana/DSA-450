class Solution:
    def pivotInteger(self, n: int) -> int:
        total_sum = (n * (n + 1))//2
        curr_sum = 0
        for i in range(1, n + 1):
            curr_sum += i
            target = (total_sum - curr_sum) + i
            if target == curr_sum:
                return i
        return -1
