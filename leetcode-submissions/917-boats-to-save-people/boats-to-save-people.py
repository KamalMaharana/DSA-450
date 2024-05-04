class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people = sorted(people)
        total = 0
        count = 0
        i = 0
        j = len(people) - 1
        while i <= j:
            if people[i]+people[j] <= limit:
                count += 1
                i += 1
                j -= 1
            else:
                j -= 1
                count += 1
                
        return count
        