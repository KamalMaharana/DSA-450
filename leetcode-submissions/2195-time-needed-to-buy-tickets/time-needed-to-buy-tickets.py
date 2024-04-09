class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        time = 0
        n = len(tickets)
        t = tickets
        while tickets[k] != 0:
            for i in range(n):
                if t[i] != 0:
                    t[i] -= 1
                    time += 1
                
                if t[k] == 0:
                    return time
        return time
