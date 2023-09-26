class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        _map = {}
        freq = Counter(s)
        stack = []
        for ch in s:
            
            if ch in _map: 
                freq[ch] -= 1
                continue
            
            while stack and stack[-1] >= ch and freq[stack[-1]] > 1:
                c = stack[-1]
                # print(stack, ch, freq[c])
                freq[c] -= 1
                _map.pop(stack.pop())
                
            if ch not in _map:
                stack.append(ch)
                _map[ch] = None

        
        return "".join(stack)
                
                # "gbagdgbg"