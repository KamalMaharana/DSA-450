class Solution:
    def pivotInteger(self, n: int) -> int:
        def get_sum(n):
            return (n * (n + 1))//2
        total_sum = get_sum(n)
        curr_sum = 0
        # 1 2 3 4 5 6 7 8 = 45 - 
        for i in range(1, n + 1):
            curr_sum += i
            target = (total_sum - curr_sum) + i
            if target == curr_sum:
                return i
        return -1
