class Solution:
    def averageWaitingTime(self, customers: List[List[int]]) -> float:
        curr_time = customers[0][0]
        wait_time = 0
        for arr, t in customers:
            if arr > curr_time:
                wait_time += t
                curr_time = arr + t
            else:
                curr_time += t
                wait_time += curr_time - arr
            
        return wait_time/len(customers)

# w = 3 + 
# 2 + 3 = 5
