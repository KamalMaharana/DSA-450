class Solution:
    def numberOfBeams(self, banks: List[str]) -> int:
        present = []
        for r in banks:
            count = 0
            for c in r:
                if c == '1':
                    count += 1
            present.append(count)
        
        prev = 0
        lasers = 0
        # print(present)
        for i in range(1, len(banks)):
            curr = i
            if present[prev] == 0:
                prev = curr
            else:
                if present[curr] != 0:
                    lasers += present[prev] * present[curr]
                    prev = curr
        return lasers
