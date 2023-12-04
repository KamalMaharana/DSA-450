class Solution:
    def largestGoodInteger(self, num: str) -> str:
        window = num[:3]
        result = ""
        if window[0] == window[1] == window[2]:
            result = window
        i = 0
        j = 3
        while j < len(num):
            window = window[1:]
            i += 1
            window += num[j]
            j += 1
            if window[0] == window[1] == window[2]:
                if not result or int(result) < int(window):
                    result = window
                # else:
                #     if int(result) < int(window):
                    
        return str(result)
