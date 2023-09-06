class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        cnt1 = 0
        cnt2 = 0
        ele1 = 0
        ele2 = 0
        n = len(nums)
        for i in nums:
            if cnt1 == 0 and i != ele2:
                cnt1 = 1
                ele1 = i
            elif cnt2 == 0 and i != ele1:
                cnt2 = 1
                ele2 = i
            elif ele1 == i:
                cnt1 += 1
            elif ele2 == i:
                cnt2 += 1
            else:
                cnt1 -= 1
                cnt2 -= 1
        
        cnt1 = 0
        cnt2 = 0
        limit = n // 3 + 1
        for i in nums:
            if i == ele1:
                cnt1 += 1
            elif i == ele2:
                cnt2 += 1
        res = []
        if cnt1 >= limit:
            res.append(ele1)
        if cnt2 >= limit:
            res.append(ele2)
        res.sort()
        return res

