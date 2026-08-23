class Solution:
    def sumGame(self, num: str) -> bool:
        l = len(num)
        left_question_mark = num[:l//2].count('?')
        right_question_mark = num[l//2:].count('?')
        total = left_question_mark + right_question_mark
        if total & 1:
            return True
        
        left_sum = 0
        right_sum = 0
        for i in range(l // 2):
            if num[i] != "?":
                left_sum += int(num[i])
            
            if num[l - i - 1] != "?":
                right_sum += int(num[l - i - 1])
        
        if (left_sum - right_sum) == ((right_question_mark - left_question_mark) // 2) * 9:
            return False
        return True