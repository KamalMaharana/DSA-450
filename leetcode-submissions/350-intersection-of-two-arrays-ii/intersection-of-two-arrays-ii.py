class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        map1 = Counter(nums1)
        map2 = Counter(nums2)
        result = []
        for i in map1:
            if i in map2:
                result += [i] * min(map1[i], map2[i])
        return result