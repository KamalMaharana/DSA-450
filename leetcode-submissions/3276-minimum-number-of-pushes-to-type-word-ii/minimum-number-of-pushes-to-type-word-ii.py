class Solution:
    def minimumPushes(self, word: str) -> int:
        freq = Counter(word)
        arr = sorted(list(word),key = lambda x: freq[x], reverse = True)
        curr_lvl = 1
        visited = dict()
        cnt = 0
        res = 0
        for c in arr:
            if c in visited:
                res += visited[c]
            else:
                visited[c] = curr_lvl
                res += visited[c]
                cnt += 1
                if cnt == 8:
                    cnt = 0
                    curr_lvl += 1
                
            # print(cnt, c, curr_lvl)
        # print(visited)
        return res