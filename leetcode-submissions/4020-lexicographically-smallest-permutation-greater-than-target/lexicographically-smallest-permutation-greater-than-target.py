from collections import Counter
class Solution:

  def lexGreaterPermutation(self, s: str, target: str) -> str:
    n = len(s)
    freq = Counter(s)
    strings = []
    
    ch = ""
    for f in freq:
        if f > target[0]:
            if ch == "":
                ch = f
            else:
                ch = min(ch, f)
    
    # print(ch)
    if ch != "":
        freq[ch] -= 1
        temp = ""
        for f in freq:
            temp += (f * freq[f])
        
        temp = sorted(temp)
        temp = "".join(temp)
        # print(ch + temp)
        strings.append(ch + temp)
        freq[ch] += 1
    
    
    for i, c in enumerate(target):
        if freq[c] > 0:
            freq[c] -= 1
            flag = 0
            temp_s = target[0:i+1]
            # print("Temp", temp_s, "Char", c)
            ch = ""
            if i + 1 < n:
                for f in freq:
                    if f > target[i + 1] and freq[f] > 0:
                        if ch == "":
                            ch = f
                        else:
                            ch = min(ch, f)
                        flag = 1
                # print(ch)
                temp_s += ch
                freq[ch] -= 1
            # print("Temp_S 48", temp_s)
            # print(i, c, ch)
            if flag:
                temp = ""
                for f in freq:
                    temp += f * freq[f]
                
                temp = sorted(temp)
                temp_s = temp_s + "".join(temp)
                # print(temp_s, ch, i+1, c)
                strings.append(temp_s)

            freq[ch] += 1
        else:
            break

    # print(strings)
    if len(strings):
        strings.sort()
        return strings[0]
    return ""
    
                