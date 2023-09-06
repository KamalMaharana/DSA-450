class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        bill_5 = 0
        bill_10 = 0
        for bill in bills:
            change_req = abs(bill - 5)
            # for 20$ bill
            if change_req == 15:
                if bill_10 > 0 and bill_5 > 0:
                    bill_10 -= 1
                    bill_5 -= 1
                elif bill_5 >= 3:
                    bill_5 -= 3
                else:
                    return False
            # For 10$ bill
            elif change_req == 5:
                if bill_5 > 0:
                    bill_5 -= 1
                    bill_10 += 1
                else:
                    return False
            else:
                bill_5 += 1
        return True