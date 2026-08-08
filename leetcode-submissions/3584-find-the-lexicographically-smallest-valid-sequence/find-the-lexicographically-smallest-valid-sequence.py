class Solution:
    def validSequence(self, word1: str, word2: str) -> List[int]:
        l1 = len(word1)
        l2 = len(word2)
        change = False
        res = []
        last = [-1] * l2
        # For every character in word2
        j = l2 - 1
        for i in range(l1 - 1, -1, -1):
            if word1[i] == word2[j]:
                last[j] = i
                j -= 1
            
            if j < 0: break
        
        # print(last)
        j = 0
        for i in range(l1):
            if j == l2: break
            # print(word1[i], word2[j])
            if word1[i] == word2[j]:
                res.append(i)
                j += 1
            elif not change and (j == l2 - 1 or last[j + 1] > i):
                # print(last[j + 1], i)
                change = True
                res.append(i)
                j += 1
        
        return res if len(res) == l2 else []