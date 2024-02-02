class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        result = []
        queue = deque(range(1,10))
        while queue:
            elem = queue.popleft()
            if low <= elem <= high:
                result.append(elem)
            last_digit = elem % 10
            if last_digit < 9: 
                new_num = elem*10 + last_digit + 1
                queue.append(new_num)
                    
        return result