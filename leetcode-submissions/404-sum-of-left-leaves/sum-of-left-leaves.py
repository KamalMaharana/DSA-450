# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        self.result = 0
        def dfs(node, isLeftchild):
            if not node:
                return
            
            if node.left == None and node.right == None and isLeftchild:
                self.result += node.val
                return
            
            dfs(node.left, True)
            dfs(node.right, False)
        
        dfs(root, False)
        return self.result