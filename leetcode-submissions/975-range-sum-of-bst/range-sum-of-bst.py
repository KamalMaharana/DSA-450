# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: TreeNode, low: int, high: int) -> int:
        # self.sums = 0
        stk, self.sums = [root], 0
        while stk:
            node = stk.pop()
            if node:
                if node.val > low:
                    stk.append(node.left)  
                if node.val < high:
                    stk.append(node.right)
                if low <= node.val <= high:
                    self.sums += node.val    
        return self.sums
#         def dfs(node, low, high):
#             if node == None:
#                 return
            
#             if node.val < low:
#                 dfs(node.right, low, high)
#             elif node.val > high:
#                 dfs(node.left, low, high)
#             else:
#                 self.sums += node.val
#                 dfs(node.left, low, high)
#                 dfs(node.right, low, high)
        
#         dfs(root, low, high)
#         return self.sums
        