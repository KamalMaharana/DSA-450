class Solution:
    def findDiagonalOrder(self, nums: List[List[int]]) -> List[int]:
        row = len(nums)
        col = 0
        _map = defaultdict(list)
        end = 0
        for i in range(row):
            for j in range(len(nums[i])):
                _map[i + j].append(nums[i][j])
                end = max(end, i + j)
        
        result = []
        # print(_map)
        for i in range(end + 1):
            result += _map[i][::-1]
        return result