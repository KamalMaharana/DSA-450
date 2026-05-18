class Solution:
    def minJumps(self, arr: List[int]) -> int:
        n = len(arr)
        queue = deque([[0, 0]])
        visited = set()
        hashmap = defaultdict(list)
        for i, val in enumerate(arr):
            hashmap[val].append(i)
        
        while queue:
            index, step = queue.popleft()
            if index == n - 1:
                return step
            if index in visited: continue
                
            visited.add(index)
            if index > 0:
                queue.append([index - 1, step + 1])
            
            queue.append([index + 1, step + 1])
            
            for i in hashmap[arr[index]]:
                if i != index and arr[i] == arr[index]:
                    queue.append([i, step + 1])
            del hashmap[arr[index]]
        return step