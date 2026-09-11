class Solution:
    def totalNumbers(self, digits: List[int]) -> int:
        count = 0
        for num in range(100, 1000, 2):
            s = str(num)
            temp = digits.copy()
            possible = True
            for ch in s:
                digit_val = int(ch)
                if digit_val in temp:
                    temp.remove(digit_val)
                else:
                    possible = False
                    break
            if possible:
                count += 1
        return count