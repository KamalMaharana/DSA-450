class Solution:
    def minOperations(self, logs: List[str]) -> int:
        level = 0
        for l in logs:
            if l == "./":
                pass
            elif l == "../":
                level = max(level - 1, 0)
            else:
                level += 1
        return level