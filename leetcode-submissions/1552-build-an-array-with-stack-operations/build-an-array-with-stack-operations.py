class Solution:
    def buildArray(self, target: List[int], n: int) -> List[str]:
        curr = 1
        result = []
        for i in target:
            while curr != i:
                result += ["Push", "Pop"]
                curr += 1
            result += ["Push"]
            curr += 1
        return result