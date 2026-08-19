from collections import defaultdict
from typing import List

class Solution:
    def maxNumberOfFamilies(self, n: int, reservedSeats: List[List[int]]) -> int:
        def possible(seats, grp):
            for i in grp:
                if i in seats:
                    return False
            return True

        # 1. Group reserved seats by row (ignoring seats 1 and 10)
        _map = defaultdict(set)
        for r, s in reservedSeats:
            if 2 <= s <= 9:
                _map[r].add(s)

        # 2. Fully unreserved rows can fit 2 groups each
        res = 2 * (n - len(_map))

        # 3. Check each row with reservations
        left_grp = (2, 3, 4, 5)
        right_grp = (6, 7, 8, 9)
        middle_grp = (4, 5, 6, 7)

        for row in _map:
            seats = _map[row]
            
            can_left = possible(seats, left_grp)
            can_right = possible(seats, right_grp)
            can_middle = possible(seats, middle_grp)

            # Greedily allocate: Left + Right (2 groups), otherwise 1 group if any fits
            if can_left and can_right:
                res += 2
            elif can_left or can_right or can_middle:
                res += 1

        return res