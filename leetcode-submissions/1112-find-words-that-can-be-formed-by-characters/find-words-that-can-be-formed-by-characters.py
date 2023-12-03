class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        freq = Counter(chars)
        result = 0
        for w in words:
            f2 = Counter(w)
            # print(freq, f2)
            flag = True
            for i in f2:
                # print(i, freq[i] >= f2[i])
                if i not in freq or freq[i] < f2[i]:
                    flag = False
            if flag:
                result += len(w)
        return result