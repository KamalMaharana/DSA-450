class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        n = len(nums)
        maxi = max(nums)
        i, j, cnt, ans = 0, 0, 0, 0


        for j in range(n):
            if nums[j] == maxi:
                cnt += 1
            
            while cnt >= k:
                if nums[i] == maxi:
                    cnt -= 1
                i += 1
            ans += i

        return ans
