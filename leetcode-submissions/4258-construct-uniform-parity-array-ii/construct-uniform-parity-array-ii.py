class Solution:
    def uniformArray(self, nums1: list[int]) -> bool:
        nums1.sort()
        # All evens
        odd = 1 if nums1[0] % 2 == 1 else 0
        for n in nums1[1:]:
            if n&1:
                if not odd:
                    return False
                odd += 1
        
        return True