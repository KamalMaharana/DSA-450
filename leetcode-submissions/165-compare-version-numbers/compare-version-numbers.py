class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        version1 = version1.split(".")
        version2 = version2.split(".")
        if len(version1) < len(version2):
            version1 += [0] * (len(version2) - len(version1))
        else:
            version2 += [0] * (len(version1) - len(version2))
        
        for i in range(len(version1)):
            v1 = int(version1[i])
            v2 = int(version2[i])
            if v1 < v2:
                return -1
            elif v1 > v2:
                return 1
        return 0