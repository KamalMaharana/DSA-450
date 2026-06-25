class Solution:
    def countMajoritySubarrays(self, nums: List[int], target: int) -> int:
        res = 0
        trgt_cnt = 0
        for i in range(len(nums)):
            trgt_cnt = 0
            for j in range(i, len(nums)):
                if nums[j] == target:
                    trgt_cnt += 1
                length = j - i + 1
                if 2 * trgt_cnt > length:
                    res += 1

        return res