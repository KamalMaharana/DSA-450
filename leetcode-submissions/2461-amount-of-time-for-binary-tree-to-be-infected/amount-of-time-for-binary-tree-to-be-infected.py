# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def amountOfTime(self, root: Optional[TreeNode], start: int) -> int:
        self.graph = defaultdict(list)
        def dfs(node):
            if not node:
                return None
            
            left = dfs(node.left)
            if left:
                self.graph[node.val].append(left.val)
                self.graph[left.val].append(node.val)
            right = dfs(node.right)
            if right:
                self.graph[node.val].append(right.val)
                self.graph[right.val].append(node.val)
            return node
        
        dfs(root)
        queue = [(start, 0)]
        visited = {start}
        res = 0
        while queue:
            node, time = queue.pop(0)
            res = max(res, time)
            for neigh in self.graph[node]:
                if neigh not in visited:
                    visited.add(neigh)
                    queue.append((neigh, time + 1))
        return res