# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        self.same = True
        
        def dfs(p_node, q_node):
            if p_node == None and q_node == None:
                return
            
            if (p_node == None and q_node != None) or (p_node != None and q_node == None) or (p_node.val != q_node.val):
                self.same = False
                return
            
            dfs(p_node.left, q_node.left)
            if self.same:
                dfs(p_node.right, q_node.right)
        
        dfs(p,q)
        return self.same
            
        