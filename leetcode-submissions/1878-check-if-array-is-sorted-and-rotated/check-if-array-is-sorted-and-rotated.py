class Solution:
    def check(self, nums: List[int]) -> bool:
        n = len(nums)
        for i in range(n):
            cnt = 0
            j = i
            prev = 0
            while cnt != n:
                curr = nums[j % n]
                if curr >= prev:
                    prev = curr
                else:
                    break
                cnt += 1
                j += 1
            if cnt == n:
                return True
        return False