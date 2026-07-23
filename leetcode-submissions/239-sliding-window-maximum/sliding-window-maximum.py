class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        queue = deque()
        for i in range(k):
            val = nums[i]
            # print(queue)
            while queue and val > nums[queue[-1]]:
                queue.pop()
            queue.append(i)
        
        i = 0
        j = k
        # print(queue)
        res = [nums[queue[0]]]
        n = len(nums)
        while j < n:
            val = nums[j]
            while queue and val > nums[queue[-1]]:
                queue.pop()
            queue.append(j)

            i += 1
            j += 1
            while queue and queue[0] < i:
                queue.popleft()
            
            # print(queue)
            res.append(nums[queue[0]])

        return res